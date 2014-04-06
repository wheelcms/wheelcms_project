from .util import get_env_variable

HAYSTACK_CONNECTIONS = {

    'default': {
        # 'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'ENGINE': 'wheelcms_axle.solr_engine.SolrEngine',
        'URL': get_env_variable('SOLR_URL', 'http://127.0.0.1:8983/solr'),
        'INCLUDE_SPELLING': True,

        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
