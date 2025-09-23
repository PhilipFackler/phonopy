try:
    import cupy
    from phonopy.acc.numba_imports import numba, cuda, use_acc
    from phonopy.acc.phonon.qpoints import run_qpoints_phonon
except ImportError:
    from phonopy.acc.dummy import use_acc, run_qpoints_phonon
