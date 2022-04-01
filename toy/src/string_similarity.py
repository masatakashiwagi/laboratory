import difflib
import zlib

import diff_match_patch as dmp_module


def gestalt_approach_matcher(sx, sy):
    """ゲシュタルトアプローチによる類似度評価"""
    gestalt_value = difflib.SequenceMatcher(None, sx, sy).ratio()

    return gestalt_value


def zlib_compress_matcher(sx, sy):
    """zlib compressによる圧縮した文字列データの類似度評価"""
    if not (isinstance(sx, bytes) and isinstance(sy, bytes)):
        sx = sx.encode('utf-8')
        sy = sy.encode('utf-8')
    ab = len(zlib.compress(sx + sy))
    a, b = len(zlib.compress(sx)), len(zlib.compress(sy))
    compress_value = 1.0 - (0.0 + a + b - ab) / max(a, b)
    compress_value = 1.0 - compress_value

    return compress_value


def levenshtein_distance_matcher(sx, sy):
    """レーベンシュタイン距離による類似度評価"""
    dmp = dmp_module.diff_match_patch()
    # Don't spend more than 0.1 seconds on a diff.
    dmp.Diff_Timeout = 0.1
    diff = dmp.diff_main(sx, sy)
    dmp.diff_cleanupSemantic(diff)
    levenshtein_value = dmp.diff_levenshtein(diff)

    str_length = len(sx) if len(sx) > len(sy) else len(sy)
    levenshtein_value = levenshtein_value / str_length
    levenshtein_value = 1.0 - levenshtein_value

    return levenshtein_value
