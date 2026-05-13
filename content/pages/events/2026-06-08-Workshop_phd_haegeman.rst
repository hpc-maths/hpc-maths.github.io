:title: Multiphase flows workshop
:category: event
:date: 2026-06-08 14:00
:place: Ecole polytechnique
:shortdescription: A mini-workshop co-organised by ONERA and CMAP on two-phase flows and related topics 


.. class:: center


:Abstract: A mini-workshop co-organised by ONERA and CMAP on two-phase flows and related topics on the occasion of the PhD defence of W. Haegeman.  


.. title:: Invited speakers

- Jean-Marc Hérard (EDF R&D) : *Schémas pour la prise en compte des termes sources dans une classe de modèles multiphasiques*
This talk presents a numerical methodology for tackling a class of compressible multiphase flow models. The targeted applications involve flows with fast transients and shock waves.
We thus consider the hyperbolic system of PDE including stiff source terms:

.. math::

    \partial_t W + \nabla \cdot (F(W)) + C(W)\nabla W = S(W) (1)

The two-step algorithm includes an explicit scheme to account for convective effects (left hand side of (1), step 1) and an implicit scheme to handle stiff relaxation effects (right hand side of (1), step 2). The core idea in the second step consists in rewriting ODEs involving the RHS of (1) as an evolution equation of the velocity / pressure / temperature / Gibbs potential gaps, together with a steady constraint. This approach has been used to compute approximate solutions of immiscible two-phase and three-phase flow models [1,2]. It has also been used for a three-field two-phase flow model that includes a non-condensable gas [3].  

References:
| [1] Jean-Marc Hérard, Guillaume Jomée. “Two approaches to compute unsteady compressible two-phase flow models with stiff relaxation terms.“ ESAIM: Mathematical Modelling and Numerical Analysis, 27:3537–3583, 2023.
| [2] Jean-Marc Hérard, Guillaume Jomée. “A coupled approach to compute approximate solutions of a compressible immiscible three-phase flow model with fast transient and stiff source terms.“, SMAI Journal of Computational Mathematics, 405-434, 2025.
| [3] Jean Bussac, Jean-Marc Hérard, Guillaume Jomée, “Numerical simulation of a hybrid two-phase flow model”, In preparation, 2026.

- Didier Bresch (LAMA, USMB)

- Ilya Peshkov (University of Trento)

- Michael Dumbser (University of Trento)

- Maren Hantke (Martin-Luther-Universität Halle-Wittenberg)



.. title:: Schedule

**14:00 - 16:00 First session** 

- 14:00 - 14:40: *Talk 1*
- 14:40 - 15:20: *Talk 2*
- 15:20 - 16:00: *Talk 3*

**16:00 - 16:30 Break** 

**16:30 - 17:50 Second session**

- 16:30 - 17:10: *Talk 4* 
- 17:10 - 17:50: *Talk 5*
