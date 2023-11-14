from flask import render_template,request, redirect, url_for
from flask_login import login_required
from . import main_bp
from .models import Groups,Groups1


@main_bp.route('/')
@login_required
def index():
    return render_template('main/index.html')
  

@main_bp.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    if request.method == 'POST':
        userid = request.form.get('userid')
        groupid = request.form.get('groupid')
        print(userid)
        print(groupid)

        result = Groups1.create(group_id=groupid, user_id=userid)

        return redirect(url_for('main.group'))

    all_groups = Groups.get_all_group_names()
    return render_template('auth/group.html', all_groups=all_groups)

