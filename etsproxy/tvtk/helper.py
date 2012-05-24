#-------------------------------------------------------------------------------
#
# Copyright (c) 2012
# IMB, RWTH Aachen University,
# ISM, Brno University of Technology
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in the Spirrid top directory "licence.txt" and may be
# redistributed only under the conditions described in the aforementioned
# license.
#
# Thanks for using Simvisage open source!
#
#-------------------------------------------------------------------------------

# ETS 3
try:
    from enthought.tvtk.api import tvtk
    from tvtk_classes import tvtk_helper
# ETS 4
except ImportError:
    from tvtk.api import tvtk
    from tvtk.tvtk_classes import tvtk_helper
