(define (square x) (* x x))


(define (average x y)
(/ (+ x y) 2))


(define (abs x)
(if (< x 0)
    (- x)
    x))


(define (sqrt x)
(define (good-enough? guess)
  (< (abs (- (square guess) x)) 0.001))
(define (improve guess)
  (average guess (/ x guess)))
(define (sqrt-iter guess)
  (if (good-enough? guess)
      guess
      (sqrt-iter (improve guess))))
(sqrt-iter 1.0))
(sqrt 9)


(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))


((lambda (x y z) (+ x y (square z))) 1 2 3)


(define (length items)
(if (null? items)
    0
    (+ 1 (length (cdr items)))))
(define (getitem items n)
(if (= n 0)
    (car items)
    (getitem (cdr items) (- n 1))))
(define squares (list 1 4 9 16 25))


(define (repeat k fn) (if (> k 0)
                          (begin (fn) (repeat (- k 1) fn))
                          nil))


(repeat 5
(lambda () (fd 100)
           (repeat 5
                   (lambda () (fd 20) (rt 144)))
           (rt 144)))


(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))     
    
(define (sier d k)
    (tri (lambda ()
            (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
    (sier (/ d 2) (- k 1))
    (penup)
    (fd d)
    (pendown))

(sier 400 6)