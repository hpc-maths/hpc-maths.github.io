:title: Battery Modeling and Simulation Seminar
:category: event
:date: 2025-05-26 14:00
:place: Salle de conférence du CMAP - Ecole polytechnique
:shortdescription: This seminar aims to bring together leading experts and young researchers from France and abroad to discuss recent advances in lithium-ion battery modeling and simulation.

.. class:: center


:Title: **Battery Modeling and Simulation Seminar**
:Abstract: This seminar aims to bring together leading experts and young researchers from France and abroad to discuss recent advances in lithium-ion battery modeling and simulation. Whether you are already involved in battery research or just beginning to explore the field, you are warmly invited to join us for an afternoon of scientific exchange. Topics will range from multi-scale and multi-physics approaches to continuum modeling and impedance analysis, addressing both theoretical challenges and practical applications. By fostering dialogue across disciplines, the seminar seeks to advance our understanding and predictive capabilities for next-generation battery systems.

Program [30 mins  presentation + 10 mins questions for each speaker]

- 14:00-14:40 Geometric optimization of a lithium-ion battery, Richard Joly, PhD student, CMAP and TotalEnergies
- 14:40-15:20 Multi-scale modeling of graphite lithiation in Li-ion batteries, Marion Chandesris, Directrice de Recherche, CEA-Liten
- 15:20-16:00 Continuum models for lithium-ion batteries: a mathematical approach, Ferran B. Planella, Professor, University of Warwick

:Abstracts:


Speaker: Richard Joly, PhD student, CMAP and TotalEnergies

 
Abstract: Striving for the improvement of the energy density of lithium-ion batteries (LIBs) and for the minimization of their charging time thanks to design, is not new. Up to date, experimental works conducted on laser-perforated electrodes showed engaging results, while technologies relying on additive manufacturing have only been tested in a few academic studies to improve the performance of LIB cells. At the same time, the burst of recent researches on the parametric and topology optimization [5] of such battery cells have allowed to hope for the numerical conception of new battery architectures, outperforming the standard planar geometry. The homogenized model of Doyle, Fuller and Newman [3] (DFN) - serves as the foundation for numerous academic and industrial softwares [6] used to simulate the operation of lithium-ion batteries during charging and discharging. Studying a battery cell Ω = Ωanode ∪Ωseparator ∪Ωcathode subject to a constant current discharge, our goal is to optimize each electrode interface by minimizing a shape dependent objective function. We propose [4] here an implementation of the so-called pseudo-3D (P3D) version of the DFN model, which combines finite-element and finite-difference methods using the FreeFEM and C++ languages. Coupled with the application of geometric optimization tools [1] to the electrode interfaces, this implementation allows us to compute a shape gradient through the adjoint method and to apply a gradient flow algorithm to minimize a performance function under geometric constraints. We impose for instance in this minimization process the non-mixing constraint [2] between the anodic domain and the cathodic domain. These computations represent a first step towards a complete geometric and topological optimization of the battery cell, including the optimization of the solid material distribution and the porous microstructure within each electrode.

 
[1] G. Allaire, C. Dapogny, and F. Jouve. Shape and topology optimization. In Geometric partial differential equations. Part 2, pages 1–132. Amsterdam: Elsevier/North Holland, 2021.
[2] F. Feppon, G. Allaire, C. Dapogny, and P. Jolivet. Body-fitted topology optimization of 2d and 3d fluid-to-fluid heat exchangers. Comput. Methods Appl. Mech. Eng., 376:36, 2021.
[3] T. F. Fuller, M. Doyle, and J. Newman. Simulation and optimization of the dual lithium ion insertion cell. Journal of the electrochemical society, 141(1):1, 1994.
[4] R. Joly, G. Allaire, and R. de Loubens. Geometric optimization of a lithium-ion battery with the doyle-fuller-newman model. 2025.
[5] H. Li, G. Bucci, N. W. Brady, N. R. Cross, V. M. Ehlinger, T. Y. Lin, M. Salazar de Troya, D. Tortorelli, M. A. Worsley, and T. Roy. Topology optimization for the full-cell design of porous electrodes in electrochemical energy storage devices. Structural and Multidisciplinary Optimization, 67(11):1–28, 2024.
[6] V. Taralova, O. Iliev, and Y. Efendiev. Derivation and numerical validation of a homogenized isothermal Li-ion battery model. J. Eng. Math., 101:1–27, 2016.



 
Speaker: Marion Chandesris, Directrice de Recherche, CEA-Liten

 
Abstract: The use of modeling and simulation tools for Li-ion batteries has grown considerably in recent years, to support the deployment of these technologies. The complexity of the phenomena at play at the heart of batteries requires the development of multi-physics models combining electrochemistry, transport of charged species, associated electric field, thermal effects, etc. Moreover, depending on the issues addressed, the scale at which these models are developed can vary greatly, from the particle of active material to the battery pack. In order to master the hypotheses associated with these different modeling scales, and also to promote the exchange of information between models, we have carried out several theoretical up-scaling work, applied to the modeling of graphite electrodes. At electrode scales, the resolution of the Newman model in the frequency domain using the Fourier transform provides an analytical expression of the impedance spectrum. From this analytical expression, it is then possible to improve the extraction of the physical properties of the materials, going beyond classical electrical equivalent model of the EIS. At the electrode scale, we apply the volume-averaging method to the microstructure-scale model of battery electrodes in order to revisit the Newman model and thus review its range of validity and limitations, particularly at high regime. Finally, at particle scale, a multi-layer Cahn-Hilliard model is used to analyze the dynamics of stagging which occurs during the graphite lithiation, and analyze its impact on both the heterogeneous lithiation of particle and the apparent kinetics of insertion.




Speaker: Ferran B. Planella, Professor, University of Warwick

 
Abstract: In order to optimise battery design and management, we need models than can provide fast and accurate predictions of the battery behaviour. However, many of the existing are posed in an ad hoc way, making them challenging to extend and prone to inconsistencies. This presentation will explore how we can leverage advanced mathematical techniques to derive and implement better models for battery design, control and characterisation.