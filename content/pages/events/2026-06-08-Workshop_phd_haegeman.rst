:title: Mini-workshop on continuum mechanics and multiphase flows
:category: event
:date: 2026-06-08 14:00
:place: Ecole polytechnique
:shortdescription: A mini-workshop co-organised by ONERA and CMAP on two-phase flows and related topics 


.. class:: center


:Abstract: A mini-workshop co-organised by ONERA and CMAP on topics related to continuum mechanics and two-phase flows on the occasion of the PhD defence of W. Haegeman.  


.. title:: Invited speakers

| **Jean-Marc Hérard (EDF R&D)** *Schémas pour la prise en compte des termes sources dans une classe de modèles multiphasiques*
| This talk presents a numerical methodology for tackling a class of compressible multiphase flow models. The targeted applications involve flows with fast transients and shock waves. We thus consider the hyperbolic system of PDE including stiff source terms:

.. math::

    \partial_t W + \nabla \cdot (F(W)) + C(W)\nabla W = S(W) \quad (1)

| The two-step algorithm includes an explicit scheme to account for convective effects (left hand side of (1), step 1) and an implicit scheme to handle stiff relaxation effects (right hand side of (1), step 2). The core idea in the second step consists in rewriting ODEs involving the RHS of (1) as an evolution equation of the velocity / pressure / temperature / Gibbs potential gaps, together with a steady constraint. This approach has been used to compute approximate solutions of immiscible two-phase and three-phase flow models [1,2]. It has also been used for a three-field two-phase flow model that includes a non-condensable gas [3].  
| 
| References:
| [1] Jean-Marc Hérard, Guillaume Jomée. “Two approaches to compute unsteady compressible two-phase flow models with stiff relaxation terms.“ ESAIM: Mathematical Modelling and Numerical Analysis, 27:3537–3583, 2023.
| [2] Jean-Marc Hérard, Guillaume Jomée. “A coupled approach to compute approximate solutions of a compressible immiscible three-phase flow model with fast transient and stiff source terms.“, SMAI Journal of Computational Mathematics, 405-434, 2025.
| [3] Jean Bussac, Jean-Marc Hérard, Guillaume Jomée, “Numerical simulation of a hybrid two-phase flow model”, In preparation, 2026.
| 
| **Didier Bresch (LAMA, USMB)**
| 
| **Ilya Peshkov (University of Trento)** *Modeling non-propagating modes with hyperbolic equations*
| We consider a few examples of first-order hyperbolic systems with special skew-symmetric structure of relaxation source terms. The dispersion relation for such systems is analyzed and it is shown that they exhibit a frequency band gap. This means that waves with frequencies falling into this band gap cannot propagate. Such models emerge in multiscale physical systems, e.g. in modeling acoustic metamaterials, plasma flows, multiphase flows with surface tension.
| 
| **Michael Dumbser (University of Trento)** *A simple and general framework for the construction of exactly div-rot-grad compatible discontinuous Galerkin finite element schemes on unstructured simplex meshes*
| We introduce a new family of discontinuous Galerkin (DG) finite element schemes for the discretization of first order systems of hyperbolic partial differential equations (PDE) on unstructured simplex meshes in two and three space dimensions that respect the two basic vector calculus identities exactly also at the discrete level, namely that the curl of the gradient is zero and that the divergence of the curl is zero. The key ingredient here is the construction of two compatible discrete nabla operators, a primary one and a dual one, both defined on general unstructured simplex meshes in multiple space dimensions. Our new schemes extend existing cell-centered finite volume methods based on corner fluxes to arbitrary high order of accuracy in space. An important feature of our new method is the fact that only two different discrete function spaces are needed to represent the numerical solution, and the choice of the appropriate function space for each variable is related to the origin and nature of the underlying PDE. The first class of variables is discretized at the aid of a discontinuous Galerkin approach, where the numerical solution is represented via piecewise polynomials of degree N and which are allowed to jump across element interfaces. This set of variables is related to those PDE which are mere consequences of the definitions, derived from some abstract scalar and vector potentials, and for which involutions like the divergence-free or the curl-free property must hold if satisfied by the initial data. The second class of variables is discretized via classical continuous Lagrange finite elements of approximation degree M=N+1 and is related to those PDE which can be derived as the Euler-Lagrange equations of an underlying variational principle.
| The primary nabla operator takes as input the data from the FEM space and returns data in the DG space, while the dual nabla operator takes as input the data from the DG space and produces output in the FEM space. The two discrete nabla operators satisfy a discrete Schwarz theorem on the symmetry of discrete second derivatives. From there, both discrete vector calculus identities follow automatically.
| We apply our new family of schemes to three hyperbolic systems with involutions: the system of linear acoustics, in which the velocity field must remain curl-free and the vacuum Maxwell equations, in which the divergence of the magnetic field and of the electric field must remain zero. In our approach, only the magnetic field will remain exactly divergence free. As a third model we study the Maxwell-GLM system of Munz et al. [1], which contains a unique mixture of curl-curl and div-grad operators and in which the magnetic field may be either curl-free or divergence-free, depending on the choice of the initial data. In all cases we prove that the proposed schemes are exactly total energy conservative and thus nonlinearly stable in the L2 norm. 
| 
| **Maren Hantke (Martin-Luther-Universität Halle-Wittenberg)**
| 

**Schedule**

**14:00 - 16:00 First session** 

- 14:00 - 14:40: *Talk 1*
- 14:40 - 15:20: *Talk 2*
- 15:20 - 16:00: *Talk 3*

**16:00 - 16:30 Break** 

**16:30 - 17:50 Second session**

- 16:30 - 17:10: *Talk 4* 
- 17:10 - 17:50: *Talk 5*

