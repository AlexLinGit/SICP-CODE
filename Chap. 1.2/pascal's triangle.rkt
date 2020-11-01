#lang sicp

(define (repeat word count)
  (cond ((< count 0) false)
        ((> count 0) (and (display word)
                          (display " ")
                          (repeat word (- count 1))))))

(define (pascal-elem n m)
  (cond ((or (> n m) (< n 0) (< m 0)) 0)
        ((or (= n m) (= n 0)) 1)
        (else (+ (pascal-elem (- n 1) (- m 1))
                 (pascal-elem n (- m 1))))))

(define (get-row-raw row column count)
  (cond ((< column 0) (display ""))
        ((> column row) (display "\n"))
        (else (let ((elem (pascal-elem count row)))
                (and (display elem)
                     (display " ")
                     (get-row-raw row (- column 1) (+ 1 count)))))))

(define (get-row row column)
  (get-row-raw row column 0))


  


