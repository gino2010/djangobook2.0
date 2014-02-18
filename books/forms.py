# coding=utf-8

from django import forms

__author__ = 'Gino'


#chapter07
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    message.error_messages = {'required': '不可以为空哦'}

    # 自定义校验内容和返回信息，clean_字段名称 命名方法
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('多写点吧, 四个单词以上，空格分隔！')
        return message
