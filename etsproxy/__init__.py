
try: # ETS 3
    import enthought.traits
    ETS_BASENAME = 'enthought.'
except ImportError: # ETS 4
    ETS_BASENAME = ''
