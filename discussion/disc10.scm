(define (factorial x)
    (cond
        ((= x 1) 1)
        ((= x 0) 1)
        (else (* x (factorial (- x 1))))))

(define (fib n)
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1)) (fib (- n 2))))))