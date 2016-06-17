;           Copyright (c) 2004, Daniel M. Bikel.
;                         All rights reserved.
; 
;                Developed at the University of Pennsylvania
;                Institute for Research in Cognitive Science
;                    3401 Walnut Street
;                    Philadelphia, Pennsylvania 19104
; 			
; 
; For research or educational purposes only.  Do not redistribute.  For
; complete license details, please read the file LICENSE that accompanied
; this software.
; 
; DISCLAIMER
; 
; Daniel M. Bikel makes no representations or warranties about the suitability of
; the Software, either express or implied, including but not limited to the
; implied warranties of merchantability, fitness for a particular purpose, or
; non-infringement. Daniel M. Bikel shall not be liable for any damages suffered
; by Licensee as a result of using, modifying or distributing the Software or its
; derivatives.
; 
((S (l VP) (l VBZ))
 (VP (l VBZ VBP VP NP))
 (NP (r VP)
     (l NP)(l S PRR PP) (r NN))
 (IN (l PP))
 (PP (l IN)
     (l PP))
 (COORD (l CC)(l CONN-CC))
 (ADJP (r JJ)
       (l ADJP))
 (ADVP (l RB)
       (l NN ))
 (SBAR (l PRR)(l COND)(l PRO))
 (* (l))
)