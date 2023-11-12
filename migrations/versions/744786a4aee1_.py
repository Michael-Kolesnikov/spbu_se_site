"""empty message

Revision ID: 744786a4aee1
Revises: 
Create Date: 2023-11-12 18:31:02.408276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744786a4aee1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('areas_of_study',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_areas_of_study'))
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('logo_uri', sa.String(length=512), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_company'))
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_courses'))
    )
    op.create_table('diploma_themes_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_diploma_themes_tags'))
    )
    op.create_table('internship_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('logo_uri', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_internship_company'))
    )
    op.create_table('internship_format',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('format', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_internship_format'))
    )
    op.create_table('internship_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_internship_tag'))
    )
    op.create_table('promo_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_promo_code'))
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tags'))
    )
    op.create_table('themes_level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_themes_level'))
    )
    op.create_table('thesis_on_review_worktype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis_on_review_worktype'))
    )
    op.create_table('worktype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_worktype'))
    )
    op.create_table('curriculum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('discipline', sa.String(length=256), nullable=False),
    sa.Column('study_year', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_curriculum_course_id_courses')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_curriculum'))
    )
    op.create_table('deadline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('worktype_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('choose_topic', sa.DateTime(), nullable=True),
    sa.Column('submit_work_for_review', sa.DateTime(), nullable=True),
    sa.Column('upload_reviews', sa.DateTime(), nullable=True),
    sa.Column('pre_defense', sa.DateTime(), nullable=True),
    sa.Column('defense', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['areas_of_study.id'], name=op.f('fk_deadline_area_id_areas_of_study')),
    sa.ForeignKeyConstraint(['worktype_id'], ['worktype.id'], name=op.f('fk_deadline_worktype_id_worktype')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_deadline'))
    )
    op.create_table('diploma_themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=512), nullable=False),
    sa.Column('description', sa.String(length=2048), nullable=True),
    sa.Column('requirements', sa.String(length=2048), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=2048), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('supervisor_thesis_id', sa.Integer(), nullable=True),
    sa.Column('consultant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_diploma_themes_author_id_users')),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], name=op.f('fk_diploma_themes_company_id_company')),
    sa.ForeignKeyConstraint(['consultant_id'], ['users.id'], name=op.f('fk_diploma_themes_consultant_id_users')),
    sa.ForeignKeyConstraint(['supervisor_id'], ['users.id'], name=op.f('fk_diploma_themes_supervisor_id_users')),
    sa.ForeignKeyConstraint(['supervisor_thesis_id'], ['users.id'], name=op.f('fk_diploma_themes_supervisor_thesis_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_diploma_themes'))
    )
    op.create_table('internships',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name_vacancy', sa.String(length=70), nullable=False),
    sa.Column('salary', sa.String(length=30), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('requirements', sa.Text(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('more_inf', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_internships_author_id_users')),
    sa.ForeignKeyConstraint(['company_id'], ['internship_company.id'], name=op.f('fk_internships_company_id_internship_company')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_internships'))
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('recipient', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=512), nullable=True),
    sa.Column('content', sa.String(length=8192), nullable=True),
    sa.ForeignKeyConstraint(['recipient'], ['users.id'], name=op.f('fk_notification_recipient_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_notification'))
    )
    op.create_table('notification_practice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=512), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('viewed', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], name=op.f('fk_notification_practice_recipient_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_notification_practice'))
    )
    op.create_table('reviewer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], name=op.f('fk_reviewer_company_id_company')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviewer_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviewer'))
    )
    op.create_table('current_thesis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=512), nullable=True),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('worktype_id', sa.Integer(), nullable=False),
    sa.Column('consultant', sa.String(length=2048), nullable=True),
    sa.Column('goal', sa.String(length=2048), nullable=True),
    sa.Column('text_uri', sa.String(length=512), nullable=True),
    sa.Column('supervisor_review_uri', sa.String(length=512), nullable=True),
    sa.Column('reviewer_review_uri', sa.String(length=512), nullable=True),
    sa.Column('presentation_uri', sa.String(length=512), nullable=True),
    sa.Column('text_link', sa.String(length=2048), nullable=True),
    sa.Column('presentation_link', sa.String(length=2048), nullable=True),
    sa.Column('code_link', sa.String(length=2048), nullable=True),
    sa.Column('account_name', sa.String(length=512), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['areas_of_study.id'], name=op.f('fk_current_thesis_area_id_areas_of_study')),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_current_thesis_author_id_users')),
    sa.ForeignKeyConstraint(['supervisor_id'], ['staff.id'], name=op.f('fk_current_thesis_supervisor_id_staff')),
    sa.ForeignKeyConstraint(['worktype_id'], ['worktype.id'], name=op.f('fk_current_thesis_worktype_id_worktype')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_current_thesis'))
    )
    op.create_table('diploma_themes_level',
    sa.Column('themes_level_id', sa.Integer(), nullable=False),
    sa.Column('diploma_themes_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diploma_themes_id'], ['diploma_themes.id'], name=op.f('fk_diploma_themes_level_diploma_themes_id_diploma_themes')),
    sa.ForeignKeyConstraint(['themes_level_id'], ['themes_level.id'], name=op.f('fk_diploma_themes_level_themes_level_id_themes_level')),
    sa.PrimaryKeyConstraint('themes_level_id', 'diploma_themes_id', name=op.f('pk_diploma_themes_level'))
    )
    op.create_table('diploma_themes_tag',
    sa.Column('diploma_themes_tag_id', sa.Integer(), nullable=False),
    sa.Column('diploma_themes_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diploma_themes_id'], ['diploma_themes.id'], name=op.f('fk_diploma_themes_tag_diploma_themes_id_diploma_themes')),
    sa.ForeignKeyConstraint(['diploma_themes_tag_id'], ['diploma_themes_tags.id'], name=op.f('fk_diploma_themes_tag_diploma_themes_tag_id_diploma_themes_tags')),
    sa.PrimaryKeyConstraint('diploma_themes_tag_id', 'diploma_themes_id', name=op.f('pk_diploma_themes_tag'))
    )
    op.create_table('internships_format',
    sa.Column('internships_format_id', sa.Integer(), nullable=False),
    sa.Column('internships_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['internships_format_id'], ['internship_format.id'], name=op.f('fk_internships_format_internships_format_id_internship_format')),
    sa.ForeignKeyConstraint(['internships_id'], ['internships.id'], name=op.f('fk_internships_format_internships_id_internships')),
    sa.PrimaryKeyConstraint('internships_format_id', 'internships_id', name=op.f('pk_internships_format'))
    )
    op.create_table('internships_tag',
    sa.Column('internships_tag_id', sa.Integer(), nullable=False),
    sa.Column('internships_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['internships_id'], ['internships.id'], name=op.f('fk_internships_tag_internships_id_internships')),
    sa.ForeignKeyConstraint(['internships_tag_id'], ['internship_tag.id'], name=op.f('fk_internships_tag_internships_tag_id_internship_tag')),
    sa.PrimaryKeyConstraint('internships_tag_id', 'internships_id', name=op.f('pk_internships_tag'))
    )
    op.create_table('thesis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.Column('name_ru', sa.String(length=512), nullable=False),
    sa.Column('name_en', sa.String(length=512), nullable=True),
    sa.Column('description', sa.String(length=4096), nullable=True),
    sa.Column('text_uri', sa.String(length=512), nullable=True),
    sa.Column('old_text_uri', sa.String(length=512), nullable=True),
    sa.Column('presentation_uri', sa.String(length=512), nullable=True),
    sa.Column('supervisor_review_uri', sa.String(length=512), nullable=True),
    sa.Column('reviewer_review_uri', sa.String(length=512), nullable=True),
    sa.Column('source_uri', sa.String(length=512), nullable=True),
    sa.Column('author', sa.String(length=512), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('reviewer_id', sa.Integer(), nullable=True),
    sa.Column('publish_year', sa.Integer(), nullable=False),
    sa.Column('recomended', sa.Boolean(), nullable=False),
    sa.Column('temporary', sa.Boolean(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('review_status', sa.Integer(), nullable=True),
    sa.Column('download_thesis', sa.Integer(), nullable=True),
    sa.Column('download_presentation', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['areas_of_study.id'], name=op.f('fk_thesis_area_id_areas_of_study')),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_thesis_author_id_users')),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_thesis_course_id_courses')),
    sa.ForeignKeyConstraint(['reviewer_id'], ['staff.id'], name=op.f('fk_thesis_reviewer_id_staff')),
    sa.ForeignKeyConstraint(['supervisor_id'], ['staff.id'], name=op.f('fk_thesis_supervisor_id_staff')),
    sa.ForeignKeyConstraint(['type_id'], ['worktype.id'], name=op.f('fk_thesis_type_id_worktype')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis'))
    )
    op.create_table('thesis_on_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.Column('thesis_on_review_type_id', sa.Integer(), nullable=True),
    sa.Column('name_ru', sa.String(length=512), nullable=False),
    sa.Column('text_uri', sa.String(length=512), nullable=True),
    sa.Column('presentation_uri', sa.String(length=512), nullable=True),
    sa.Column('source_uri', sa.String(length=512), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('reviewer_id', sa.Integer(), nullable=True),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('review_status', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['areas_of_study.id'], name=op.f('fk_thesis_on_review_area_id_areas_of_study')),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_thesis_on_review_author_id_users')),
    sa.ForeignKeyConstraint(['reviewer_id'], ['reviewer.id'], name=op.f('fk_thesis_on_review_reviewer_id_reviewer')),
    sa.ForeignKeyConstraint(['supervisor_id'], ['staff.id'], name=op.f('fk_thesis_on_review_supervisor_id_staff')),
    sa.ForeignKeyConstraint(['thesis_on_review_type_id'], ['thesis_on_review_worktype.id'], name=op.f('fk_thesis_on_review_thesis_on_review_type_id_thesis_on_review_worktype')),
    sa.ForeignKeyConstraint(['type_id'], ['worktype.id'], name=op.f('fk_thesis_on_review_type_id_worktype')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis_on_review'))
    )
    op.create_table('tag',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('thesis_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name=op.f('fk_tag_tag_id_tags')),
    sa.ForeignKeyConstraint(['thesis_id'], ['thesis.id'], name=op.f('fk_tag_thesis_id_thesis')),
    sa.PrimaryKeyConstraint('tag_id', 'thesis_id', name=op.f('pk_tag'))
    )
    op.create_table('thesis_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('current_thesis_id', sa.Integer(), nullable=True),
    sa.Column('was_done', sa.String(length=2048), nullable=True),
    sa.Column('planned_to_do', sa.String(length=2048), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=2048), nullable=True),
    sa.Column('comment_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name=op.f('fk_thesis_report_author_id_users')),
    sa.ForeignKeyConstraint(['current_thesis_id'], ['current_thesis.id'], name=op.f('fk_thesis_report_current_thesis_id_current_thesis')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis_report'))
    )
    op.create_table('thesis_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thesis_id', sa.Integer(), nullable=True),
    sa.Column('thesis_on_review_id', sa.Integer(), nullable=True),
    sa.Column('o1', sa.Integer(), nullable=True),
    sa.Column('o1_comment', sa.String(length=1024), nullable=True),
    sa.Column('o2', sa.Integer(), nullable=True),
    sa.Column('o2_comment', sa.String(length=1024), nullable=True),
    sa.Column('t1', sa.Integer(), nullable=True),
    sa.Column('t1_comment', sa.String(length=1024), nullable=True),
    sa.Column('t2', sa.Integer(), nullable=True),
    sa.Column('t2_comment', sa.String(length=1024), nullable=True),
    sa.Column('p1', sa.Integer(), nullable=True),
    sa.Column('p1_comment', sa.String(length=1024), nullable=True),
    sa.Column('p2', sa.Integer(), nullable=True),
    sa.Column('p2_comment', sa.String(length=1024), nullable=True),
    sa.Column('verdict', sa.Integer(), nullable=False),
    sa.Column('overall_comment', sa.String(length=1024), nullable=True),
    sa.Column('review_file_uri', sa.String(length=512), nullable=True),
    sa.ForeignKeyConstraint(['thesis_id'], ['thesis.id'], name=op.f('fk_thesis_review_thesis_id_thesis')),
    sa.ForeignKeyConstraint(['thesis_on_review_id'], ['thesis_on_review.id'], name=op.f('fk_thesis_review_thesis_on_review_id_thesis_on_review')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis_review'))
    )
    op.create_table('thesis_task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_text', sa.String(length=2048), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('current_thesis_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['current_thesis_id'], ['current_thesis.id'], name=op.f('fk_thesis_task_current_thesis_id_current_thesis')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_thesis_task'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('thesis_task')
    op.drop_table('thesis_review')
    op.drop_table('thesis_report')
    op.drop_table('tag')
    op.drop_table('thesis_on_review')
    op.drop_table('thesis')
    op.drop_table('internships_tag')
    op.drop_table('internships_format')
    op.drop_table('diploma_themes_tag')
    op.drop_table('diploma_themes_level')
    op.drop_table('current_thesis')
    op.drop_table('reviewer')
    op.drop_table('notification_practice')
    op.drop_table('notification')
    op.drop_table('internships')
    op.drop_table('diploma_themes')
    op.drop_table('deadline')
    op.drop_table('curriculum')
    op.drop_table('worktype')
    op.drop_table('thesis_on_review_worktype')
    op.drop_table('themes_level')
    op.drop_table('tags')
    op.drop_table('promo_code')
    op.drop_table('internship_tag')
    op.drop_table('internship_format')
    op.drop_table('internship_company')
    op.drop_table('diploma_themes_tags')
    op.drop_table('courses')
    op.drop_table('company')
    op.drop_table('areas_of_study')
    # ### end Alembic commands ###
