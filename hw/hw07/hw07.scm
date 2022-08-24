(define (filter-lst fn lst)
    (cond
        ((eq? lst nil) nil)
        ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
        (else (filter-lst fn (cdr lst)))
        )
    )

;;; Tests
(define (even? x)
    (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
    (cond
        ((eq? first nil) second)
        ((eq? second nil) first)
        (else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))))
        )
    )

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
    (define (helper combiner start n term current)
        (if (= current n)
            (combiner (term n) start)
            (combiner (term current) (helper combiner start n term (+ current 1)))))
    (helper combiner start n term 1)
    )


(define (no-repeats lst)
    (if (eq? lst nil)
        nil
        (begin (define res (no-repeats (cdr lst)))
               (cons (car lst) (filter-lst (lambda (x) (not (= x (car lst)))) res)))
        )
    )

