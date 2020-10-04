# Django Authenticate

```
from django.contrib.auth import authenticate, login
user = authenticate(username='john', password='secret')
if user is not None:
        login(request, user)
        # Redirect to a success page.
else:
    # Return an 'invalid login' error message.
```

```
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
```

```
if request.user.is_authenticated:
    # Do something for authenticated users
else:
    # Do something for anonymous users
```

```
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

check_password(password, u.password)
```

# Next Path in URL
```
from django.conf import settings
from django.shortcuts import redirect
def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```

# Loging Using Django Decorator
```
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def my_view(request):
    pass
```


# Django Paginator
```
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
post = Post.objects.all()
paginator = Paginator(post, 10)
try:
    page = request.GET.get('page', 1)
    post_list = paginator.page(page)
except PageNotAnInteger:
    post_list = paginator.page(1)
except EmptyPage:
    post_list = paginator.page(paginator.num_pages)

HTML Side Code
<p align="center">
{% if post_list.has_other_pages %}
{% if post_list.has_previous %}
<a href="?page={{ post_list.previous_page_number }}" class="w3-button w3-black w3-padding-large w3-margin-bottom">Previous</a>
{% endif %}
&nbsp;&nbsp;&nbsp;&nbsp;
{% if post_list.has_next %}
<a href="?page={{ post_list.next_page_number }}" class="w3-button w3-black w3-padding-large w3-margin-bottom">Next</a>
{% endif %}
{% endif %}
</p>
```


# Django Cache
```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

python manage.py createcachetable
```

```
Redis Cache
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04

>>> pip install django-redis-cache
```


# Django Message Framework
```
from django.contrib import messages
from django.contrib.messages import get_messages

messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')

HTML Side Code
{% if messages %}
<ul>
   {% for message in messages %}
	   <li>{{ message }}</li>
   {% endfor %}
</ul>
{% endif %}


Outside of templates
storage = get_messages(request)
for message in storage:
    print(message)
```


# Django Admin Customize
https://medium.com/@renjithsraj/how-to-reset-password-in-django-bd5e1d6ed652

```
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
admin/
```

# IP & Browser Detect
```
pip install httpagentparser
```

# Swagger
```
http://127.0.0.1:8000/swagger/
```

# Ref Docs
```
https://drf-yasg.readthedocs.io/en/stable

swagger(?P<format>\.json|\.yaml) [name='schema-json']
swagger/ [name='schema-swagger-ui']
redoc/ [name='schema-redoc']
```


# JWT 
```
https://pypi.org/project/djangorestframework-simplejwt
```

# JSON API
```
https://pypi.org/project/djangorestframework-jsonapi/
```

```
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
HTTP_308_PERMANENT_REDIRECT

HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_426_UPGRADE_REQUIRED
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_506_VARIANT_ALSO_NEGOTIATES
HTTP_507_INSUFFICIENT_STORAGE
HTTP_508_LOOP_DETECTED
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
HTTP_510_NOT_EXTENDED
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED

https://www.django-rest-framework.org/api-guide/status-codes/
```

