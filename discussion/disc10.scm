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

(define (my-append a b)
    (define (helper a b)
        (if (eq? (cdr a) nil)
            (cons (car a) b)
            (cons (car a) (helper (cdr a) b))))

    (cond
        ((eq? a nil) b)
        ((eq? b nil) a)
        (else (helper a b))
        ))

(define (duplicate lst)
    (cond
        ((eq? lst nil) nil)
        ((eq? (cdr lst) nil) (cons (car lst) (cons (car lst) nil)))
        (else (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
        ))

(define (insert element lst index)
    (cond
        ((= index 0) (cons element lst))
        ((eq? lst nil) nil)
        (else (insert element (cdr lst) (- index 1)))))