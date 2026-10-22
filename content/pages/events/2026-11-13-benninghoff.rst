:title: Second order explicit stabilized multirate method for stiff differential equations with error control
:category: event
:date: 2026-11-13 14:00
:place: Salle de conférence CMAP (aile5, 2e étage)
:speaker: Mathieu Benninghoff (Université de Genève)
:shortdescription: Exposé dans le cadre du séminaire HPC@Maths.

.. title:: Second order explicit stabilized multirate method for stiff differential equations with error control

Semi-discretization of parabolic problems often leads to large and stiff systems of ODEs. Standard explicit methods then require very small time steps for stability, while implicit methods allow larger steps but involve solving linear systems. Explicit stabilized methods provide an efficient compromise by enlarging the stability region while remaining fully explicit. However, when local spatial mesh refinement is introduced, their efficiency decreases, since the stiffness is driven by only the smallest mesh element. A natural approach is to split the system into fast stiff and slower mildly stiff components. In this context, Abdulle, Grote, and Rosilho de Souza (2022) proposed the first-order multirate explicit stabilized method (mRKC). We extend their approach to second order and introduce the new multirate ROCK2 method (mROCK2), which achieves high precision and allows a step-size strategy with error control.
