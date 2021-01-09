from flask import flash, current_app, render_template
from flask.globals import session
from flask_wtf import file

from FAT.database import db
from FAT.forms import MemberForm
from FAT.models import Member

from werkzeug.utils import redirect, secure_filename
from azure.storage.blob import BlockBlobService


@current_app.route('/')
def index():
    members = Member.query.all()
    return render_template('members/list.html', members=members)

@current_app.route('/add', methods=['GET', 'POST'])
def add_member():
    if not session.get('user'):
        return redirect('/auth/login')

    form = MemberForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        height = form.height.data
        weight = form.weight.data

        new_member = Member(first_name=first_name, last_name=last_name, age=age, height=height, weight=weight)
        db.session.add(new_member)
        db.session.flush()

        if form.profile_picture.data:
            try:
                f = form.profile_picture.data
                extension = f.filename.split('.')[-1]
                filename = f'{new_member.id}.{extension}'

                blob_account = current_app.config['BLOB_ACCOUNT']
                blob_key = current_app.config['BLOB_KEY']
                blob_name = current_app.config['BLOB_NAME']
                blob_service = BlockBlobService(account_name=blob_account, account_key=blob_key)
                blob_service.create_blob_from_stream(blob_name, filename, f)
            except Exception as e:
                current_app.logger.error(f'Failed to upload image to blob : {e}')
                flash('Something went wrong', "danger")
                return redirect('/')

            new_member.profile_pic = filename

        flash('Added new member', "info")
        db.session.commit()
        return redirect('/')

    return render_template('members/add.html', form=form)

@current_app.route('/delete/<id>')
def delete_member(id):
    if not session.get('user'):
        return redirect('/auth/login')

    try:
        member = Member.query.get(id)
        profile_pic = member.profile_pic
        db.session.delete(member)
        db.session.commit()
        if profile_pic:
            try:
                blob_account = current_app.config['BLOB_ACCOUNT']
                blob_key = current_app.config['BLOB_KEY']
                blob_name = current_app.config['BLOB_NAME']
                blob_service = BlockBlobService(account_name=blob_account, account_key=blob_key)
                blob_service.delete_blob(blob_name, profile_pic)
                current_app.logger.info(f'Removed file {profile_pic} from AzureBlob')
            except Exception as e:
                flash('Failed to remove image from server. Do it manualy')
                current_app.logger.error(f'Failed to remove image from blob: {e}')
        flash('Removed member', 'info')
    except Exception as e:
        current_app.logger.error(f'Failed to remove record: {e}')
        flash('Failed to remove given member', 'danger')
    return redirect('/')