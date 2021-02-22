# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.conf import settings
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from .models import Topic, Appendix, ForumAvatar, Post, Notification
from django.utils.translation import ugettext as _
from django import forms

if 'pagedown' in settings.INSTALLED_APPS:
    use_pagedown = True
    from django import forms
    from pagedown.widgets import PagedownWidget
else:
    use_pagedown = False


class TopicForm(ModelForm):
    if use_pagedown:
        content_raw = forms.CharField(label=_('Content'), widget=PagedownWidget())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TopicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Topic
        fields = ['node', 'title', 'content_raw']
        labels = {
            'content_raw': _('Content'),
            'node': _('Node'),
            'title': _('Title'),
        }

    def save(self, commit=True):
        inst = super(TopicForm, self).save(commit=False)
        inst.user = self.user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class TopicEditForm(ModelForm):
    if use_pagedown:
        content_raw = forms.CharField(label=_('Content'), widget=PagedownWidget())

    def __init__(self, *args, **kwargs):
        super(TopicEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Topic
        fields = ('content_raw',)
        labels = {
            'content_raw': _('Content'),

        }


class AppendixForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.topic = kwargs.pop('topic', None)
        super(AppendixForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Appendix
        fields = ('content_raw',)
        labels = {
            'content_raw': _('Content'),
        }

    def save(self, commit=True):
        inst = super(AppendixForm, self).save(commit=False)
        inst.topic = self.topic
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class ForumAvatarForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ForumAvatarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = ForumAvatar
        fields = ('image', 'use_gravatar')
        labels = {
            'image': _('Avatar Image'),
            'use_gravatar': _("Always Use Gravatar")
        }

    def save(self, commit=True):
        inst = super(ForumAvatarForm, self).save(commit=False)
        inst.user = self.user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class ReplyForm(ModelForm):
    if use_pagedown:
        content_raw = forms.CharField(label='', widget=PagedownWidget())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.topic_id = kwargs.pop('topic_id', None)
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Post
        fields = ('content_raw',)
        labels = {
            'content_raw': '',
        }

    def save(self, commit=True):
        inst = super(ReplyForm, self).save(commit=False)
        inst.user = self.user
        inst.topic_id = self.topic_id
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class NotificationsForm(ModelForm):
    # if use_pagedown:
    #     content_raw = forms.CharField(label='', widget=PagedownWidget())

    def __init__(self, *args, **kwargs):
        self.post_id = kwargs.pop('post_id', None)
        self.sender_id = kwargs.pop('sender_id', None)
        self.to_id = kwargs.pop('to_id', None)
        self.topic_id = kwargs.pop('topic_id', None)
        super(NotificationsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Notification
        fields = '__all__'

        def save(self, commit=True):
            inst = super(ForumAvatarForm, self).save(commit=False)
            inst.post_id = self.post_id
            inst.sender_id = self.sender_id
            inst.to_id = self.to_id
            inst.topic_id = self.topic_id
            if commit:
                inst.save()
                self.save_m2m()
            return inst


# 添加一下登录窗口的输入验证
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='用户名',
        error_messages={
            'required': '用户名不能为空'
        }
    )
    password = forms.CharField(
        required=True,
        label='密码',
        error_messages={
            'required': '密码不能为空',

        })


# 注册表单验证
class RegForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='用户名',
        min_length=3,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '用户名必须大于3位数'
        }
    )
    password1 = forms.CharField(
        required=True,
        min_length=6,
        label='密码',
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码必须大于6位数'
        })
    password2 = forms.CharField(
        required=True,
        min_length=6,
        label='密码',
        error_messages={
            'required': '确认密码不能为空',
            'min_length': '确认密码必须大于6位数'
        })

    email = forms.EmailField(
        required=True,
        min_length=6,
        label='密码',
        error_messages={
            'required': '邮箱不能为空',
            'min_length': '邮箱必须大于6位数'
        }
    )

    def clean(self):
        password_value = self.cleaned_data.get('password1')
        re_password_value = self.cleaned_data.get('password2')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('password2', '两次密码不一致')
            raise ValidationError('两次密码不一致')
