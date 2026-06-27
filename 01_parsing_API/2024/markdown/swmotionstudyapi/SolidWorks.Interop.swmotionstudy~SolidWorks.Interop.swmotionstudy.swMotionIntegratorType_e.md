---
title: "swMotionIntegratorType_e Enumeration"
project: "SOLIDWORKS Motion Study API Help"
interface: "swMotionIntegratorType_e"
member: ""
kind: "enum"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.swMotionIntegratorType_e.html"
---

# swMotionIntegratorType_e Enumeration

Integration methods for solving numerically stiff systems.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMotionIntegratorType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMotionIntegratorType_e
```

### C#

```csharp
public enum swMotionIntegratorType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMotionIntegratorType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMotionIntegrator_GSTIFF | 1 = Default integration method for fast and accurate computation of displacements; variable order and step size; coefficients are calculated assuming a constant step size |
| swMotionIntegrator_SI2_GSTIFF | 3 = Stabilized Index-2 integration method that provides better error control over the velocity and acceleration terms in equations of motion; provided motion is sufficiently smooth, velocity and acceleration results are more accurate than those computed with GSTIFF or WSTIFF; significantly slower |
| swMotionIntegrator_WSTIFF | 2 = Variable order and step size integration method; coefficients are calculated as a function of the step size; handles sudden step size changes as a result of discontinuities or abrupt events without error or loss of accuracy |

## See Also

[SolidWorks.Interop.swmotionstudy Namespace](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html)
