from django.shortcuts import render, get_object_or_404, redirect
from .models import Message

# Create your views here.
def messages(request):
    '''
    교집합, 차집합
    q1. 메시지의 받는사람 값 (보낸이 : 나)
    q2. 메시지의 보낸사람 값 (받는이 : 나)

    차집합 -> 새로운 사람들 값 <- 쿼리로 존재하지 않음.. 리스트?
    m1 = message.filter (받: 나 and 보: 새로운)
    m2 = message.filter (보: 나 and 받: 새로운)  
    결과 = m1 + m2
    '''

    ### 무시 ###
    receive_messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    send_messages = Message.objects.filter(sender=request.user).order_by('-created_at')
    # messages = messages.order_by('-sender')
    
    '''
    유저별로 묶되, 유저의 정렬 기준은 메시지의 최신 순서여야 한다.
    '''

    return render(request, 'messages.html', {'receive_messages': receive_messages, 'send_messages': send_messages})

def show(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    other = message.receiver if message.sender == request.user else message.sender
    return render(request, 'show.html', {'message': message, 'other': other})

def messagecreate(request, user_id):
    from django.contrib.auth.models import User
    from .forms import MessageForm

    user = get_object_or_404(User, pk=user_id)
    if request.method=='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.receiver = user
            message.sender = request.user
            message.save()
            return redirect('message:messages')
        else:
            return redirect('list', user_id=request.user.id)
    else:
        form = MessageForm()
        return render(request, 'new.html', {'form': form, 'user': user})