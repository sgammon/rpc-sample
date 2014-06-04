# -*- coding: utf-8 -*-

'''

  base classes

'''

# canteen
from canteen import rpc, model
from canteen.rpc import premote as proto
from canteen.util.struct import BidirectionalEnum


##### !!! Enums !!! #####
class Auth(BidirectionalEnum):

  ''' specifies possible levels of requirement/elevation
      for privilege protection. '''

  OPTIONAL = 0x0  # no credentials required at all
  REQUIRED = 0x1  # any valid credentials required
  INTERNAL = 0x2  # internal adsnative credentials



##### !!! Base Model !!! #####
class BaseModel(model.Model):

  ''' base model class '''

  __adapter__ = 'InMemoryAdapter' if __debug__ else 'RedisAdapter'

  @classmethod
  def factory(cls, parent=None, id=None, **kwargs):

    '''  '''

    # figure out key ID and parent
    id, parent = (
      parent if (not id or (isinstance(basestring, parent) and not parent)) else id,
      parent if not isinstance(parent, basestring) else None
    )

    # inject ID if we have one
    if hasattr(cls, 'id'): kwargs['id'] = id

    # factory object
    return cls(key=model.Key(cls, id, parent=parent), **kwargs)

Model = BaseModel


##### !!! Base Service !!! #####

## +=+ Auth Exceptions +=+ ##
class Unauthorized(proto.ApplicationError):

  ''' raised when authentication credentials
      aren't properly authorized to run a given
      method. '''


class AuthenticationRequired(proto.RequestError):

  ''' raised when authentication credentials
      are required, but were not provided at all. '''


## +=+ Base Service +=+ ##
class Service(rpc.Service):

  ''' base service class '''

  __credentials__ = None  # credentials pulled via `initialize`

  exceptions = rpc.Exceptions({
    # Base Exceptions
    'unauthorized': Unauthorized,
    'auth_required': AuthenticationRequired
  })

  @property
  def credentials(self):

    ''' property getter for request credentials '''

    return self.__credentials__ or Credentials()

  def initialize(self, state):

    ''' initialize service transport state

        takes one of these:
        https://developers.google.com/appengine/docs/python/tools/protorpc/remote/requeststateclass

        or one of these if running over HTTP (likely):
        https://developers.google.com/appengine/docs/python/tools/protorpc/remote/httprequeststateclass '''

    # this is where we would interpret and mount authentication

  def enforce(self, request, level):

    ''' enforce authentication state interpreted
        by `Service.initialize`.

        :raises Unauthorized: if a method's credentials are not sufficiently privileged
        to complete the operation as-requested.

        :raises AuthenticationRequired: if a method requires authentication and no
        credentials are provided at all. '''

    # enforce authentication/authorization (mounted by `initialize`)

  @classmethod
  def protect(cls, level=Auth.OPTIONAL):

    ''' class-level decorator to transparently apply auth protection of various levels
        to an otherwise-public service method. '''

    def _protected_method(cls, inner):

      ''' wraps a protected method (``inner``) and attempts to validate
          previously-mounted credentials, by decorating the requested
          remote procedure with `Service.enforce`, which raises exceptions
          if auth requirements are not satisifed. '''

      def wrapped(self, request):

        ''' inner wrapped method that applies the proper dispatch and
            security enforcement flow. '''

        # optional: no auth required, don't need to call `enforce`
        if level is Auth.OPTIONAL: return inner(request)

        # required: authenticate, returning result or excepting out
        if self.enforce(request, level): return inner(request)

      wrapped.__name__, wrapped.__doc__ = inner.__name__, inner.__doc__
      return wrapped
    return _protected_method


# bring up to module-level for syntactic sugar
protect = Service.protect
