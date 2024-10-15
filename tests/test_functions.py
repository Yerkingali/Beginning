from problems import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False

def test_primes():
    assert len(primes(5)) == 5
    assert primes(5) == [2, 3, 5, 7, 11]

def test_checksum():
    assert checksum([1, 2, 6, 24]) == 6012369

def test_pipeline():
    assert pipeline() == 7785816
