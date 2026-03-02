:title: Flash workshop around kinetic theory
:category: event
:date: 2026-02-02 14:00
:place: Salle de conférence du CMAP - École polytechnique
:shortdescription: This one-day workshop aims to bring together leading experts and young researchers from France and abroad to discuss recent advances in kinetic theory and related models.

.. class:: center


:Title: **Flash Workshop around kinetic theory**

Program [45mins  presentation + 5 mins questions]

- 14:00-14:50 Aldo Frezzotti (Politecnico di Milano): *Kinetic theory applications to liquid-vapor flows*
- 14:50-15:40 Vincent Giovangigli (CMAP - École polytechnique): *Kinetic derivation of Cahn-Hilliard fluid models*
- 16:00-16:50 Giuseppe Orlando (CMAP - École polytechnique): *A unified compressible two-phase, two-scale model with capillarity for separated-to-disperse transitions in atomizing flows*
- 16:50-17:40 Daniele Biasone (ONERA/CMAP - École polytechnique): *Assessment of moment closures for shock structure prediction in transition-regime rarefied flows* 

:Abstracts:


Speaker: Aldo Frezzotti (Politecnico di Milano)

| Title: Kinetic theory applications to liquid-vapor flows

Abstract: The aim of the talk is to present the applications of mathematical and numerical models, based on the kinetic theory of fluids, to two-phase flows. Here, sharp liquid-vapor interfaces and ubiquitous Knudsen layers create macroscopic variables jumps, on the scale of the mean free path. The presentation is divided into two parts. The first one is devoted to summarize the results of studies based on a sort of ”standard model”. The latter consists in describing the ideal vapor phase by the Boltzmann equation (or a kinetic model). The coupling with the liquid phase is described by phenomenological boundary conditions. The model properties are discussed and compared with experimental results as well as with molecular dynamics simulations. The second part of the talk is devoted to describe models that provide a unified, albeit approximate, description of both phases, including a fully resolved liquid-vapor interface. Particular attention is given to the Enskog-Vlasov equation which gives an approximate description of a fluid composed by atoms interacting through the Sutherland potential, whose attractive tail allow the model to have solutions in which liquid and vapor phases coexist, separated by a smooth interface. The model properties are presented together with a recent attempt to derive a set of moment equations, based on Grad26 closure. Preliminary results about solutions of the local and non-local form of the linearized moment equation are presented for simple flows.




Speaker: Vincent Giovangigli (CMAP - École polytechnique)

| Title: Kinetic derivation of Cahn-Hilliard fluid models

Abstract: We present the derivation of Cahn-Hilliard fluid equations from the kinetic theory of dense gas mixtures. The fluid equations involves a Cahn-Hilliard gradient energy, Cahn-Hilliard diffusive fluxes, a Korteweg type tensor, and a Dunn and Serrin type heat flux. The Chapman-Enskog procedure is used with a proper scaling of the generalized Boltzmann equations obtained from the BBGKY hierarchy together with higher order Taylor expansions of pair distribution functions. The main steps of the derivation are presented and an Euler/van der Waals model is obtained at zeroth order while the Cahn-Hilliard model is obtained at first order. The resulting Cahn-Hilliard fluid equations involve species masses, momentum and energy conservation equations and are also compatible with the thermodynamic of irreversible processes.




Speaker: Giuseppe Orlando (CMAP - École polytechnique)

| Title: A unified compressible two-phase, two-scale model with capillarity for separated-to-disperse transitions in atomizing flows

Abstract: We present a two-phase, two-scale compressible flow model with surface tension, enabling a unified description of both separated-interface and disperse-phase regimes. The formulation is derived in the isothermal setting and builds upon Hamilton’s Stationary Action Principle. Inter-scale mass-transfer terms, activated when local curvatures exceed a grid-independent cutoff length scale, allow for the transition from the large-scale representation to the small-scale disperse regime. This mechanism ensures the regularization of the large-scale interface while simultaneously modeling atomization through the formation of a spray of droplets at the small scale. The proposed process is dissipative for the extended thermodynamics which includes surface energies. The model has been implemented in the samurai code. We demonstrate its capabilities on a relevant test case. Perspectives and on-going work for extending the methodology to full thermodynamics will also be addressed.




Speaker: Daniele Biasone (ONERA/CMAP - École polytechnique)

| Title: Assessment of moment closures for shock structure prediction in transition-regime rarefied flows

Abstract: Modern gas dynamics increasingly demands numerical models capable of resolving flowfields with space-varying levels of rarefaction, as commonly encountered in aerospace applications such as spacecraft propulsion systems, where gas expands from dense continuum conditions inside the combustion chamber to highly rarefied regimes near the nozzle exit. In such hybrid dense–rarefied environments, classical continuum or fully kinetic approaches alone are often either inaccurate or computationally prohibitive. Moment methods provide an appealing alternative, offering a macroscopic formulation enriched with non-equilibrium effects while remaining computationally efficient across a wide range of flow regimes.

This work investigates the performance of several closure techniques for the five-moment system in the prediction of steady one-dimensional shock structures in supersonic rarefied gases within the transition regime. The closures examined include the classical Grad and linearized Grad models, as well as the HMBMM,Bi-Gaussian, and HyQMOM formulations.

The methods are systematically assessed and compared in terms of accuracy, robustness, and computational efficiency. Four benchmark configurations are considered, spanning two Mach numbers and two Knudsen numbers representative of transition regime conditions. Accuracy is evaluated through direct comparison with deterministic solutions of the BGK equation obtained using the Discrete VelocityMethod, providing a consistent kinetic reference.

In addition, to improve the predictive quality of moment-based simulations, a realizability-preserving second-order MUSCL-type reconstruction is introduced. The proposed approach systematically enhances spatial accuracy across all closures while maintaining the physical admissibility of the moment set.

[1] C. Berthon. “Stability of the MUSCL Schemes for the Euler Equations”. In: Communications in Mathematical Sciences 3.2 (June 2005), pp. 133–157. url: https://www.math.sciences.univ-nantes.fr/~berthon/articles/MUSCL.pdf.

[2] P. L. Bhatnagar, E. P. Gross, and M. Krook. “A Model for Collision Processes in Gases”. In: Physical Review 94.3 (May 1954), pp. 511–525. issn: 0031-899X. doi: 10.1103/physrev.94.511.

[3] Z. Cai. “Moment method as a numerical solver: Challenge from shock structure problems”. In: Journal of Computational Physics 444 (Nov. 2021), p. 110593. issn: 0021-9991. doi: 10.1016/j.jcp.2021.110593.

[4] C. Chalons et al. “Multivariate Gaussian Extended Quadrature Method of Moments for Turbulent Disperse Multiphase Flow”. In: Multiscale Modeling & Simulation 15.4 (Jan. 2017), pp. 1553–1583. issn: 1540-3467. doi: 10.1137/16m109209x.

[5] R.O. Fox, F. Laurent, and A. Vié. “Conditional hyperbolic quadrature method of moments for kinetic equations”. In: Journal of Computational Physics 365 (July 2018), pp. 269–293. issn: 0021-9991. doi: 10.1016/j.jcp.2018.03.025.

[6] H. Grad. “On the kinetic theory of rarefied gases”. In: Communications on Pure andApplied Mathematics 2.4 (Dec. 1949), pp. 331–407. issn: 1097-0312. doi: 10.1002/cpa.3160020403.

[7] Z.Hu, Z. Cai, and Y. Wang. “Numerical Simulation of Microflows Using Hermite SpectralMethods”. In: SIAM Journal on Scientific Computing 42.1 (Jan. 2020), B105–B134. issn: 1095-7197. doi: 10.1137/18m120066x.

[8] L. Mieussens. “Discrete velocity model and implicit scheme for the BGK equation of rarefied gas dynamics”. In: Mathematical Models and Methods in Applied Sciences 10.08 (Nov. 2000), pp. 1121–1149. issn: 1793-6314. doi: 10.1142/s0218202500000562.