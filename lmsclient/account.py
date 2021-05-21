import attr

from .base import Base


@attr.s
class Account(Base):
    """Class with account attributes"""

    name = attr.ib(default="")
    sis_account_id = attr.ib(default="")
    default_storage_quota_mb = attr.ib(default="")
    default_user_storage_quota_mb = attr.ib(default="")
    default_group_storage_quota_mb = attr.ib(default="")
