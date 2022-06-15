# Copyright 2019 Google LLC.
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

"""Tests for tink.python.tink.hybrid_key_templates."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
from absl.testing import parameterized
from tink.proto import common_pb2
from tink.proto import ecies_aead_hkdf_pb2
from tink.proto import tink_pb2
from tink import aead
from tink import hybrid
from tink.testing import helper


class HybridKeyTemplatesTest(parameterized.TestCase):

  @parameterized.parameters([
      ('ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM',
       hybrid.hybrid_key_templates.ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM),
      ('ECIES_P256_COMPRESSED_HKDF_HMAC_SHA256_AES128_GCM',
       hybrid.hybrid_key_templates
       .ECIES_P256_COMPRESSED_HKDF_HMAC_SHA256_AES128_GCM),
      ('ECIES_P256_HKDF_HMAC_SHA256_AES128_CTR_HMAC_SHA256',
       hybrid.hybrid_key_templates
       .ECIES_P256_HKDF_HMAC_SHA256_AES128_CTR_HMAC_SHA256),
      ('ECIES_P256_COMPRESSED_HKDF_HMAC_SHA256_AES128_CTR_HMAC_SHA256',
       hybrid.hybrid_key_templates
       .ECIES_P256_COMPRESSED_HKDF_HMAC_SHA256_AES128_CTR_HMAC_SHA256)

  ])
  def test_template(self, template_name, template):
    self.assertEqual(template,
                     helper.template_from_testdata(template_name, 'hybrid'))

  def test_create_aes_eax_key_template(self):
    # Intentionally using 'weird' or invalid values for parameters,
    # to test that the function correctly puts them in the resulting template.
    template = hybrid.hybrid_key_templates.create_ecies_aead_hkdf_key_template(
        curve_type=common_pb2.NIST_P521,
        ec_point_format=common_pb2.DO_NOT_USE_CRUNCHY_UNCOMPRESSED,
        hash_type=common_pb2.SHA1,
        dem_key_template=aead.aead_key_templates.AES256_EAX)
    self.assertEqual(
        'type.googleapis.com/google.crypto.tink.EciesAeadHkdfPrivateKey',
        template.type_url)
    self.assertEqual(tink_pb2.TINK, template.output_prefix_type)
    key_format = ecies_aead_hkdf_pb2.EciesAeadHkdfKeyFormat.FromString(
        template.value)
    self.assertEqual(key_format.params.kem_params.curve_type,
                     common_pb2.NIST_P521)
    self.assertEqual(key_format.params.kem_params.hkdf_hash_type,
                     common_pb2.SHA1)
    self.assertEqual(key_format.params.ec_point_format,
                     common_pb2.DO_NOT_USE_CRUNCHY_UNCOMPRESSED)
    self.assertEqual(key_format.params.dem_params.aead_dem,
                     aead.aead_key_templates.AES256_EAX)


if __name__ == '__main__':
  absltest.main()
