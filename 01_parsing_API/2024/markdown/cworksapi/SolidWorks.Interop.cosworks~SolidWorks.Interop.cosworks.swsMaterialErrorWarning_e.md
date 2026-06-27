---
title: "swsMaterialErrorWarning_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMaterialErrorWarning_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialErrorWarning_e.html"
---

# swsMaterialErrorWarning_e Enumeration

Material errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMaterialErrorWarning_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMaterialErrorWarning_e
```

### C#

```csharp
public enum swsMaterialErrorWarning_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMaterialErrorWarning_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMaterialErrorWarningCreepWithForceControl | 24 = Creep option for material works only with force control method ; error |
| swsMaterialErrorWarningDefineCurveForEx | 10 = Define curve for EX; error |
| swsMaterialErrorWarningDefinePointForStressStrainCurve | 16 = Define point (0,0) for this stress-strain curve; error |
| swsMaterialErrorWarningDefineProperty | 6 = Define at least one property; error |
| swsMaterialErrorWarningDefineStressStrainCurve | 15 = Define stress-strain curve for material; error |
| swsMaterialErrorWarningDensityNotDefined | 13 = Material density not defined; error |
| swsMaterialErrorWarningEXNotDefined | 8 = EX (modulus of elasticity) not defined; error |
| swsMaterialErrorWarningEXValue | 9 =EX should be > 0; error |
| swsMaterialErrorWarningFatigueSNCurvesCycles | 3 = Cycle values of fatigue S-N curves should be monotonically increasing ; error |
| swsMaterialErrorWarningInvalidLinearElasticAnisotropicMaterialModel | 1 = The linear elastic anisotropic material model is invalid for this study ; error |
| swsMaterialErrorWarningInvalidMaterialModel | 2 = Invalid material model for this study; error |
| swsMaterialErrorWarningMaterialPropertyValue | 7 = Material property value should be > 0; error |
| swsMaterialErrorWarningMaterialTemperatureCurveForNitinol | 11 = Material temperature curve is not allowed for Nitinol; error |
| swsMaterialErrorWarningMaterialTemperatureDependencyIgnored | 30 = Material temperature dependency is ignored for drop test analysis ; warning |
| swsMaterialErrorWarningNUXYNotDefined | 32 = Poisson's Ratio (NUXY) is not defined; program will use a default value of 0.0 ; warning |
| swsMaterialErrorWarningNUXYValue | 12 = NUXY (Poissons Ratio) should be < 0.5; error |
| swsMaterialErrorWarningOnlyBilinearPlasticityForDropTestStudies | 31 = Only bilinear plasticity is supported for drop test studies; stress-strain curves are ignored ; warning |
| swsMaterialErrorWarningrKXNotDefined | 14 = KX (thermal conductivity) not defined; error |
| swsMaterialErrorWarningSIGC_F2LessThanSIGC_S2 | 23 = Property SIGC_F2 should be less than SIGC_S2 ; error |
| swsMaterialErrorWarningSIGC_S1LessThanSIGC_F1 | 21 = Property SIGC_S1 should be less than SIGC_F1 ; error |
| swsMaterialErrorWarningSIGC_S2LessThanSIGC_F1 | 22 = Property SIGC_S2 should be less than SIGC_F1 ; error |
| swsMaterialErrorWarningSIGT_F2LessThanSIGT_S2 | 20 = Property SIGT_F2 should be less than SIGT_S2 ; error |
| swsMaterialErrorWarningSIGT_S1_F1_S2_F2Values | 17 = Properties SIGT_S1, SIGT_F1, SIGT_S2 and SIGT_F2 should be > 0 ; error |
| swsMaterialErrorWarningSIGT_S1LessThanSIGT_F1 | 18 = Property SIGT_S1 should be less than SIGT_F1 ; error |
| swsMaterialErrorWarningSIGT_S2LessThanSIGT_F1 | 19 = Property SIGT_S2 should be less than SIGT_F1 ; error |
| swsMaterialErrorWarningSuccessful | 0 = Successful |
| swsMaterialErrorWarningTooManyPointsSNCurve | 5 = S-N curves should not have more than 200 data points; error |
| swsMaterialErrorWarningUniqueStressRatioForEachSNCurve | 4 = Stress ratio should be unique for each S-N curve; error |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
