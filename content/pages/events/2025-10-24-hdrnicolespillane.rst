:title: Soutenance d'Habilitation à Diriger des Recherches: High Performance Krylov Subspace Solvers with Preconditioning and Deflation
:category: event
:date: 2026-10-24 14:00
:place: École polytechnique - amphithéatre Becquerel
:speaker: Nicole Spillane (CMAP)
:shortdescription: Soutenance d'Habilitation à Diriger des Recherches

.. title:: Résumé de l'exposé


Keysords : 
linearsystem, Krylov subspace solver, GMRES, deflation, convergence, preconditioning, parallel computing

Abstract :
Linear solvers are an essential tool for the accurate numerical simulation of large scale problems. My work addresses the analysis, development and application of linear solvers for problems that arise in science or the industry. My particular focus is on a class of iterative linear solvers called the Krylov Subspace Methods. Together with the accelerators that are preconditioning and deflation, Krylov subspace methods offer a flexible framework for a wide range of problem. The contributions in this manuscript divide into three main topics.
A first set of results is for symmetric positive definite matrices solved by the conjugate gradient method preconditioned by domain decomposition. A unified theory of spectral coarse spaces is developed, a new fully algebraic solver is introduced, and open-source software is made available to apply these methods.
The second set of results addresses multipreconditioning, a technique that allows to exploit not just one, but several preconditioners. At each iteration, the space in which the solution is optimized grows much faster than with classical preconditioning. This can significantly accelerate convergence but multipreconditioned iterations are also more expensive. A significant contribution is adaptive multipreconditioning in which it is decided on the fly whether to apply a preconditioner or a multipreconditioner. This work is most advanced for symmetric positive definite problem but non-symmetric preconditioners and non-symmetric problems are also considered.
Finally, the last set of results is for non-Hermitian problems solved by GMRES. Convergence of GMRES is still not fully predictable for general matrices despite it having been an active field of research for many years already. The contributions in this manuscript are new convergence bounds that make apparent the role played by the preconditioner, the deflation operator and the choice of a weighted inner product. An important finding is that, if the matrix is positive definite, it is a good strategy to precondition its Hermitian part with a Hermitian positive definite preconditioner. Convergence then depends on how well the Hermitian part is preconditioned and on how non-Hermitian the problem is. Finally, a new spectral deflation space is proposed to improve the term in the bound that depends on the non-Hermitianness of the problem. This has the effect of accelerating convergence in practice too.


The presentation will be followed by a discussion with the members of the jury:
* Grégoire Allaire, Professor at École polytechnique
* Stéphanie Chaillat, CNRS Senior Researcher at ENSTA
* Marc Embree, Professor at Virginia Tech
* Virginie Erlacher, Professor at École des Ponts
* Martin Gander, Professor at Université de Genève
* Luc Giraud, Senior Researcher at Inria Bordeaux
* Laura Grigori, Professor at EPFL
* Axel Klawonn, Professor at University of Cologne
