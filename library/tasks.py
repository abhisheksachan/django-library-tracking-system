from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task
def check_overdue_loans():
    print("starrting check for overdue email")
    current_date = timezone.now()
    loans = Loan.objects.filter(is_returned=False, due_date__lte=current_date).select_related('book', 'member__user')

    for loan in loans:
        member_email = loan.member.user.email
        book_title = loan.book.title
        try:
            send_mail(
                subject='Book Overdue',
                message=f'Hello {loan.member.user.username},\n\nYou have not returned book "{book_title}", which was due on {loan.due_date}.\nPlease return it asap to avoid penalties.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
             )
        except Exception:
            print(f"Unable to send email for loan: {loan.pk}")