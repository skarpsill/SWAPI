---
title: "Get PMI Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_PMI_Data_Example_CSharp.htm"
---

# Get PMI Data Example (C#)

This example shows how to get Product and Manufacturing Information (PMI) from a Step 242 file.

```vb
  // ----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a Step 242 file that contains PMI annotations.
 // 2. Open an Immediate window.
  // 3. Add breakpoints as needed and press F10 to walk through the macro.
 //
 // Postconditions:
 // Inspect the Immediate window for PMI annotations, if available.
  // ----------------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Diagnostics;
 using System.Globalization;
 using System.IO;
 using System.Linq;
 using System.Reflection;
 using System.Runtime.CompilerServices;
 using System.Security;
 using System.Text;
 using System.Threading.Tasks;
 using Microsoft.VisualBasic;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace GetPMIData_CSharp
 {
     partial class SolidWorksMacro
 {
     private ModelDoc2 swModel;
     private ModelDocExtension swModelDocExt;
     private Annotation swAnnotation;
     private PMIDatumData swPMIDatumData;
     private PMIDatumFeature swPMIDatumFeature;
     private PMIDatumTarget swPMIDatumTarget;
     private PMIDimensionData swPMIDataDim;
     private PMIDimensionItem swPMIDataDimItem;
     private PMIGtolData swPMIDataGtol;
     private PMIGtolBoxData swPMIGtolBoxData;
     private PMIFrameData swPMIFrameData;
     private PMIGtolFrameDatum swPMIGtolFrameDatum;
     private int IAnnoPMIType;
     private int iAnnoCnt;
     private object[] arrAnnotation;
     private int i;
     private int j;
     private int k;
     private int l;
     private int IAnnoType;

     public void Main()
     {
         swModel = (ModelDoc2)swApp.ActiveDoc;
         swModelDocExt = swModel.Extension;

         iAnnoCnt = swModelDocExt.GetAnnotationCount();

         if (iAnnoCnt > 0)
         {
             arrAnnotation = (object[])swModelDocExt.GetAnnotations();

             for (i = 0; i <= arrAnnotation.GetUpperBound(0); i++)
             {
                 swAnnotation = (Annotation)arrAnnotation[i];

                 IAnnoType = swAnnotation.GetType();

                 IAnnoPMIType = swAnnotation.GetPMIType();

                 switch (IAnnoType)
                 {
                     case 1:
                         {
                             Debug.Print("Annotation: Thread");
                             break;
                         }

                     case 2:
                         {
                             Debug.Print("Annotation: Datum Tag " + swAnnotation.GetName());

                             if (IAnnoPMIType == 2)
                             {
                                 swPMIDatumData = (PMIDatumData)swAnnotation.GetPMIData();

                                 Debug.Print("PMI datum data");

                                 if (swPMIDatumData.GetDatumType() == (int)swPMIDatumType_e.swPMIDatumType_DatumFeature)
                                 {

                                     // Get IPMIDatumFeature

                                     swPMIDatumFeature = (PMIDatumFeature)swPMIDatumData.GetDatumFeature();
                                     Debug.Print(" Datum feature");
                                     Debug.Print("  Label: " + swPMIDatumFeature.Label);
                                     Debug.Print("  Leader anchor style as defined in swPMIDatumAnchorStyle_e: " + swPMIDatumFeature.LeaderAnchorStyle);
                                     Debug.Print("  Leader bend length: " + swPMIDatumFeature.LeaderBendLength);
                                     Debug.Print("  Datum shape as defined in swPMIDatumShape_e: " + swPMIDatumFeature.Shape);
                                     Debug.Print("  Datum text: " + swPMIDatumFeature.Text);
                                 }

                                 if (swPMIDatumData.GetDatumType() == (int)swPMIDatumType_e.swPMIDatumType_DatumTarget)
                                 {

                                     // Get IPMIDatumTarget

                                     swPMIDatumTarget = (PMIDatumTarget)swPMIDatumData.GetDatumTarget();

                                     Debug.Print(" Datum target");
                                     Debug.Print("  Area style as defined in swPMIDatumTargetAreaStyle_e: " + swPMIDatumTarget.AreaStyle);
                                     Debug.Print("  Diameter: " + swPMIDatumTarget.Diameter);
                                     Debug.Print("  Height: " + swPMIDatumTarget.Height);
                                     Debug.Print("  Movable style as defined in swPMIDatumTargetMovableStyle_e: " + swPMIDatumTarget.MovableStyle);
                                     Debug.Print("  Symbol style as defined in swPMIDatumTargetSymbolStyle_e: " + swPMIDatumTarget.SymbolStyle);
                                     Debug.Print("  Width: " + swPMIDatumTarget.Width);
                                 }

                                 Debug.Print("");
                             }
                             else if (IAnnoPMIType == 0)
                             {
                                 if (swPMIDatumData == null)
                                     Debug.Print("   No PMI data");
                                 else
                                     Debug.Print("   PMIDatumData object returned In Error");
                             }
                             else
                                 Debug.Print("   Wrong PMI data type");
                             break;
                         }

                     case 3:
                         {
                             Debug.Print("Annotation: Datum Target Symbol");
                             break;
                         }

                     case 4:
                         {
                             Debug.Print("Annotation: Display Dimension " + swAnnotation.GetName());

                             if (IAnnoPMIType == 1)
                             {
                                 swPMIDataDim = (PMIDimensionData)swAnnotation.GetPMIData();

                                 if (swPMIDataDim != null)
                                 {
                                     for (k = 0; k <= swPMIDataDim.GetDimensionItemCount() - 1; k++)
                                     {
                                         swPMIDataDimItem = (PMIDimensionItem)swPMIDataDim.GetDimensionItemAtIndex(k);

                                         Debug.Print("  Dimension item " + k);
                                         Debug.Print("    Text: " + swPMIDataDim.DimensionText);
                                         Debug.Print("    Instance count: " + swPMIDataDimItem.InstanceCount);
                                         Debug.Print("    Tolerance type as defined in swTolType_e: " + swPMIDataDimItem.TolType);
                                         Debug.Print("    Value: " + swPMIDataDimItem.Value);
                                         Debug.Print("    Value precision: " + swPMIDataDimItem.ValuePrecision);
                                         Debug.Print("    Units: " + swPMIDataDimItem.Unit);
                                         Debug.Print("    Minimum tolerance: " + swPMIDataDimItem.MinVariation);
                                         Debug.Print("    Maximum tolerance: " + swPMIDataDimItem.MaxVariation);
                                         Debug.Print("    Tolerance precision: " + swPMIDataDimItem.TolerancePrecision);
                                         Debug.Print("    Symbol as defined in swDimensionSymbol_e: " + swPMIDataDimItem.Symbol);
                                         Debug.Print("    Additional symbol as defined in swToleranceZoneModifier_e: " + swPMIDataDimItem.AdditionalSymbol);
                                         Debug.Print("    Prefix: " + swPMIDataDimItem.Prefix);
                                         Debug.Print("    Suffix: " + swPMIDataDimItem.Suffix);
                                         Debug.Print("    Callout: " + swPMIDataDimItem.CalloutText);
                                         Debug.Print("");
                                     }
                                 }
                             }
                             else if ((IAnnoPMIType == 0))
                             {
                                 if (swPMIDataDim == null)
                                     Debug.Print("   No PMI data");
                                 else
                                     Debug.Print("   PMIDimensionData object returned in error");
                             }
                             else
                                 Debug.Print("   Wrong PMI data type");
                             break;
                         }

                     case 5:
                         {
                             Debug.Print("Annotation: Gtol " + swAnnotation.GetName());

                             if (IAnnoPMIType == 3)
                             {
                                 swPMIDataGtol = (PMIGtolData)swAnnotation.GetPMIData();

                                 if (swPMIDataGtol != null)
                                 {
                                     Debug.Print("  Is composite? " + swPMIDataGtol.IsComposite());
                                     Debug.Print("  Text: " + swPMIDataGtol.GetText());
                                     Debug.Print("  Text below frames: " + swPMIDataGtol.GetTextBelowFrames());
                                     Debug.Print("  Instance count: " + swPMIDataGtol.InstanceCount);
                                     Debug.Print("  Leader location as defined in swPMILeaderLocation_e: " + swPMIDataGtol.LeaderLocation);
                                     Debug.Print("  Leader modifier as defined in swPMILeaderModifier_e: " + swPMIDataGtol.LeaderModifier);
                                     Debug.Print("  Leader style as defined in swPMILeaderStyle_e: " + swPMIDataGtol.LeaderStyle);
                                     Debug.Print("  Leader type as defined in swPMILeaderType_e: " + swPMIDataGtol.LeaderType);

                                     int iFrameCount;
                                     iFrameCount = swPMIDataGtol.GetFrameCount();

                                     Debug.Print("  Frame count is " + iFrameCount);

                                     if (iFrameCount == 0)
                                         Debug.Print("Gtol frame count is zero - API error");

                                     for (j = 0; j <= swPMIDataGtol.GetFrameCount() - 1; j++)
                                     {
                                         swPMIFrameData = (PMIFrameData)swPMIDataGtol.GetFrameAtIndex(j);
                                         if (swPMIFrameData != null)
                                         {
                                             Debug.Print("  Gtol frame " + j + " data");
                                             Debug.Print("    Geometric characteristic as defined in swGeometricCharacteristic_e: " + swPMIFrameData.GeometricCharacteristic);
                                             Debug.Print("    Frame number: " + swPMIFrameData.FrameNumber);

                                             // Get IPMIGtolBoxData

                                             for (k = 0; k <= swPMIFrameData.GetGtolBoxCount() - 1; k++)
                                             {
                                                 swPMIGtolBoxData = (PMIGtolBoxData)swPMIFrameData.GetGtolBoxAtIndex(k);
                                                 Debug.Print("    Gtol box " + k);
                                                 Debug.Print("      Material modifier as defined in swMaterialModifier_e: " + swPMIGtolBoxData.MaterialModifier);
                                                 Debug.Print("      Tolerance: " + swPMIGtolBoxData.TolValue);
                                                 Debug.Print("      Units as defined in swPMIUnit_e: " + swPMIGtolBoxData.Unit);
                                                 Debug.Print("      Tolerance zone modifier as defined in swToleranceZoneModifier_e: " + swPMIGtolBoxData.ToleranceZoneModifier);
                                                 Debug.Print("      Tolerance per unit area type as defined in swPMITolPerUnitAreaType_e: " + swPMIGtolBoxData.TolerancePerUnitType);
                                                 Debug.Print("      Tolerance 1 per unit area value: " + swPMIGtolBoxData.TolerancePerUnitValue1);
                                                 Debug.Print("      Tolerance 2 per unit area value: " + swPMIGtolBoxData.TolerancePerUnitValue2);
                                             }

                                             // Get IPMIGtolFrameDatum

                                             for (l = 0; l <= swPMIFrameData.GetGtolDatumCount() - 1; l++)
                                             {
                                                 swPMIGtolFrameDatum = (PMIGtolFrameDatum)swPMIFrameData.GetGtolDatumAtIndex(l);
                                                 Debug.Print("    Gtol frame datum " + l);
                                                 Debug.Print("      Datum: " + swPMIGtolFrameDatum.Datum);
                                                 Debug.Print("      Material modifier as defined in swMaterialModifier_e: " + swPMIGtolFrameDatum.DatumModifier);
                                                 Debug.Print("      Material modifier value if present: " + swPMIGtolFrameDatum.DatumModifierValue);
                                                 Debug.Print("      First linked datum: " + swPMIGtolFrameDatum.DatumLinked1);
                                                 Debug.Print("      Material modifier of first linked datum as defined in swMaterialModifier_e: " + swPMIGtolFrameDatum.DatumLinkedModifier1);
                                                 Debug.Print("      Value, if present, of material modifier of first linked datum: " + swPMIGtolFrameDatum.DatumLinkedModifierValue1);
                                                 Debug.Print("      Second linked datum: " + swPMIGtolFrameDatum.DatumLinked2);
                                                 Debug.Print("      Material modifier of second linked datum as defined in swMaterialModifier_e: " + swPMIGtolFrameDatum.DatumLinkedModifier2);
                                                 Debug.Print("      Value, if present, of material modifier of second linked datum: " + swPMIGtolFrameDatum.DatumLinkedModifierValue2);
                                             }
                                         }
                                         else
                                             Debug.Print("Gtol frame retrieval error");
                                     }
                                 }
                             }
                             else if (IAnnoPMIType == 0)
                             {
                                 if (swPMIDataGtol == null)
                                     Debug.Print("   No PMI data");
                                 else
                                     Debug.Print("   PMIGtolData object returned in error");
                             }
                             else
                                 Debug.Print("   Wrong PMI data type");
                             break;
                         }

                     case 6:
                         {
                             Debug.Print("Annotation: Note");
                             break;
                         }

                     case 7:
                         {
                             Debug.Print("Annotation: SF Symbol");
                             break;
                         }

                     case 8:
                         {
                             Debug.Print("Annotation: Weld Symbol");
                             break;
                         }

                     case 9:
                         {
                             Debug.Print("Annotation: Custom Symbol");
                             break;
                         }

                     case 10:
                         {
                             Debug.Print("Annotation: Dowel Symbol");
                             break;
                         }

                     case 11:
                         {
                             Debug.Print("Annotation: Leader");
                             break;
                         }

                     case 12:
                         {
                             Debug.Print("Annotation: Block");
                             break;
                         }

                     case 13:
                         {
                             Debug.Print("Annotation: Centermark symbol");
                             break;
                         }

                     case 14:
                         {
                             Debug.Print("Annotation: Table");
                             break;
                         }

                     case 15:
                         {
                             Debug.Print("Annotation: Centerline");
                             break;
                         }

                     case 16:
                         {
                             Debug.Print("Annotation: Datum Origin");
                             break;
                         }
                 }
             }
         }
     }

     /// <summary>
     ///     ''' The SldWorks swApp variable is pre-assigned for you.
     ///     ''' </summary>
     public SldWorks swApp;
 }

 }
```
