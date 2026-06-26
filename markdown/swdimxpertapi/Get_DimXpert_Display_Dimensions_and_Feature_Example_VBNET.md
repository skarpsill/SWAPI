---
title: "Get DimXpert Display Dimensions and Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm"
---

# Get DimXpert Display Dimensions and Feature Example (VB.NET)

This example shows how to find out if an annotation is a DimXpert display
dimension, and, if so, how to get its DimXpert feature.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' kadov_tag{{<spaces>}}1. Add SolidWorks.Interop.swdimxpert.dll as a reference
'    (in the Project Explorer, right-click References and click Add Reference >
'     .NET tab). kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt
' kadov_tag{{<spaces>}}3. Click View > Toolbars > DimXpert.
' kadov_tag{{<spaces>}}4. Click Auto Dimension Scheme on the DimXpert toolbar.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5. Make sure Chamfer is selected in Feature Filters
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}on the Auto Dimension Scheme PropertyManager page,
'    then click the checkmark to close the page.
'
' Postconditions: Adds DimXpert display dimensions to the model.
'
' NOTE: Because this part document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdimxpert
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swPart As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAnnotation As Annotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDisplayDimension As DisplayDimension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAnnotation = swPart.GetFirstAnnotation2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Do While (Not (swAnnotation Is Nothing))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Annotation name = " & swAnnotation.GetName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If swAnnotationType_e.swDisplayDimension = swAnnotation.GetType Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Is a display dimension? True")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDisplayDimension = swAnnotation.GetSpecificAnnotation
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case (swDisplayDimension.Type2)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swOrdinateDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = base ordinate and its subordinates")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swLinearDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = linear")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swAngularDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}= angular")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swArcLengthDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = arc length")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swRadialDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = radial")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swDiameterDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = diameter")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swHorOrdinateDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = horizontal ordinate")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swVertOrdinateDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = vertical ordinate")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swZAxisDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = z-axis")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swChamferDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = chamfer dimension")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swHorLinearDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = horizonal linear")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swVertLinearDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = vertical linear")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimensionType_e.swScalarDimension
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = scalar")
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Display dimension type = unknown")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Is a DimXpert display dimension? " & IIf(swDisplayDimension.IsDimXpert = False, "False", "True"))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If swAnnotation.IsDimXpert Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Dim DimXpertFeat As DimXpertFeature
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Dim FeatName As String
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}DimXpertFeat = swAnnotation.GetDimXpertFeature()
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}If Not DimXpertFeat Is Nothing Then
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}FeatName = DimXpertFeat.Name
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature name = " & FeatName)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Select Case (DimXpertFeat.Type)
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Plane
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = plane")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Cylinder
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = cylinder")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Cone
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = cone")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Extrude
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = extrude")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Fillet
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = fillet")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Chamfer
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = chamfer")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = compound hole")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = compound width")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = compound notch")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = compound closed-slot 3D")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = intersect point")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = intersect line")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = intersect circle")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = intersect plane")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Pattern
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = pattern")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Sphere
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = sphere")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = best-fit plane")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case swDimXpertFeatureType_e.swDimXpertFeature_Surface
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = surface")
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}DimXpert feature type = unknown")
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Not a display dimension")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAnnotation = swAnnotation.GetNext3
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Loop
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
