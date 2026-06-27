---
title: "Get DimXpert Display Dimensions and Feature (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm"
---

# Get DimXpert Display Dimensions and Feature (C#)

This example shows how to find out if an annotation is a DimXpert display
dimension, and, if so, how to get its DimXpert feature.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add SolidWorks.Interop.swdimxpert.dll as a reference
//   (in the Project Explorer, kadov_tag{{</spaces>}}right-click References and click Add Reference).
// 2. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
// 3. Click View > Toolbars > DimXpert.
// 4. Click Auto Dimension Scheme on kadov_tag{{</spaces>}}the DimXpert toolbar.
// 5. Make sure Chamfer is selected in Feature Filters
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}on the Auto Dimension Scheme PropertyManager page, then
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}click the checkmark to close the page.
//
// Postconditions: Adds DimXpert display dimensions o the model.
//
// NOTE: Because this part document is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdimxpert;
using System;
using System.Diagnostics;
namespace GetDimXpertFeatureAnnotationCSharp.csproj
{
partial class SolidWorksMacro
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swPart = default(ModelDoc2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Annotation swAnnotation = default(Annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayDimension swDisplayDimension = default(DisplayDimension);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAnnotation = (Annotation)swPart.GetFirstAnnotation2();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}while (((swAnnotation != null)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Annotation name = " + swAnnotation.GetName());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int AnnotationType = (int)swDimensionType_e.swDimensionTypeUnknown;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AnnotationType = swAnnotation.GetType();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (AnnotationType == (int)swAnnotationType_e.swDisplayDimension)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Is a display dimension? True");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDisplayDimension = (DisplayDimension)swAnnotation.GetSpecificAnnotation();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch ((swDisplayDimension.Type2))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swOrdinateDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = base ordinate and its subordinates");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swLinearDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = linear");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swAngularDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}= angular");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swArcLengthDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = arc length");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swRadialDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = radial");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swDiameterDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = diameter");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swHorOrdinateDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = horizontal ordinate");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swVertOrdinateDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = vertical ordinate");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swZAxisDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = z-axis");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swChamferDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = chamfer dimension");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swHorLinearDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = horizontal linear");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swVertLinearDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = vertical linear");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDimensionType_e.swScalarDimension:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = scalar");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Display dimension type = unknown");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Is a DimXpert display dimension? " + (swDisplayDimension.IsDimXpert() == false ? "False" : "True"));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (swAnnotation.IsDimXpert())
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}DimXpertFeature DimXpertFeat = default(DimXpertFeature);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}string FeatName = null;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}DimXpertFeat = (DimXpertFeature)swAnnotation.GetDimXpertFeature();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if ((DimXpertFeat != null))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}FeatName = DimXpertFeat.Name;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature name = " + FeatName);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}switch ((DimXpertFeat.Type))
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Plane:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = plane");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Cylinder:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = cylinder");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Cone:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = cone");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Extrude:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = extrude");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Fillet:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = fillet");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Chamfer:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = chamfer");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = compound hole");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = compound width");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = compound notch");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = compound closed-slot 3D");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = intersect point");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = intersect line");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = intersect circle");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = intersect plane");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Pattern:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = pattern");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Sphere:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = sphere");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = best-fit plane");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertFeatureType_e.swDimXpertFeature_Surface:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = surface");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" DimXpert feature type = unknown");
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Not a display dimension");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAnnotation = (Annotation)swAnnotation.GetNext3();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public SldWorks swApp;
}
}
```
