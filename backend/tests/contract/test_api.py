from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename

def test_openapi_spec():
    # The path is relative to the root of the project, where pytest is run from
    spec_path = 'specs/001-saas-data-quality/contracts/api.yaml'
    spec_url, spec_dict = read_from_filename(spec_path)
    validate(spec_url)
