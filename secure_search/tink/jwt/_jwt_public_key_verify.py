# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Interface for JwtPublicKeyVerify."""

from __future__ import absolute_import
from __future__ import division
# Placeholder for import for type annotations
from __future__ import print_function

import abc

from typing import Text

import six

from tink.jwt import _jwt_validator
from tink.jwt import _verified_jwt


@six.add_metaclass(abc.ABCMeta)
class JwtPublicKeyVerify(object):
  """Interface for verifying a signed JWT.

  Sees RFC 7519 and RFC 7515. Security guarantees: similar to PublicKeyVerify.
  """

  @abc.abstractmethod
  def verify_and_decode(
      self, compact: Text,
      validator: _jwt_validator.JwtValidator) -> _verified_jwt.VerifiedJwt:
    """Verifies, validates and decodes a signed compact JWT token.

    The JWT is validated against the rules in validator. That is, every claim in
    validator must also be present in the JWT. For example, if validator
    contains an issuer (iss) claim, the JWT must contain an identical claim.
    The JWT can contain claims that are NOT in the validator, which are then
    ignored. However, if the JWT contains a list of audiences, the validator
    must also contain an audience in the list.

    If the JWT contains timestamp claims such as expiration (exp), issued_at
    (iat) or not_before (nbf), they will also be validated. Validator allows to
    set a clock skew, to deal with small clock differences among different
    machines.

    Args:
      compact: A signed token encoded in the JWS compact serialization format.
      validator: A JwtValidator that validates the token.

    Returns:
      A VerifiedJwt.
    Raises:
      tink.TinkError if the operation fails.
    """
    raise NotImplementedError()
