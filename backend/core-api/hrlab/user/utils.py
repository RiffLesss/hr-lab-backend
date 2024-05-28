from rest_framework_simplejwt.tokens import RefreshToken

from hrlab.user.models import User
from hrlab import settings


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refreshToken': str(refresh),
        'accessToken': str(refresh.access_token),
        'refreshTokenExpiresIn': 172800,
        'accessTokenExpiresIn': 7200,
    }
