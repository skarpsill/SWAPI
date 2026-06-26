---
title: "DimXpert Annotation Data Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_AnnotationData_Module_CSharp.htm"
---

# DimXpert Annotation Data Module Example (C#)

```vb
// This module is a component of
// Get DimXpert Features and Annotations in a Model Example (C#).

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swdimxpert;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections.ObjectModel;
public class DimXpertAnnotationData
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// Returns a collection of Strings containing the annotations data
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private Collection<string> strs = new Collection<string>();
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Clear(Collection<string> strs)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Remove(strs[strs.Count]);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (!(strs.Count == 0))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Clear(strs);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public Collection<string> AnnotationData(DimXpertAnnotation annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDimXpertAnnotationType_e annoType = default(swDimXpertAnnotationType_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((!(strs.Count == 0)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Clear(strs);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//General info
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}GeneralInfo(annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotation.Type;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (annoType == swDimXpertAnnotationType_e.swDimXpertDatum)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DatumData((DimXpertDatum)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Position)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PositionData((DimXpertPositionTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompositePositionData((DimXpertCompositePositionTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SymmetryData((DimXpertSymmetryTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ConcentricityData((DimXpertConcentricityTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}LineProfileData((DimXpertLineProfileTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompositeLineProfileData((DimXpertCompositeLineProfileTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SurfaceProfileData((DimXpertSurfaceProfileTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompositeSurfaceProfileData((DimXpertCompositeSurfaceProfileTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity | annoType ==
swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism | annoType ==
swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}OrientationData((DimXpertOrientationTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}TotalRunoutData((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CircularRunoutData((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FlatnessData((DimXpertFlatnessTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CircularityData((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CylindricityData((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StraightnessData((DimXpertStraightnessTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}TangencyData((DimXpertTangencyTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// any of the dimension tolerance types
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimensionToleranceData((DimXpertDimensionTolerance)annotation, (DimXpertPart) dimXpertPart);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return strs;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void GeneralInfo(DimXpertAnnotation annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string annoType = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Feature modelObj = default(Feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Name: " + annotation.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = annotationTypeNameFromObject(annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Type: " + annoType);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Display Entity: " + DisplayEntity(annotation));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Is Suppressed: " + (annotation.IsSuppressed() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Inspection Dimension: " + (annotation.IsToBeInspected() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Is Statistical: " + (annotation.IsStatistical() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Is FreeState: " + (annotation.IsFreeState() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelObj = (Feature)annotation.GetModelFeature();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((modelObj != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void DatumData(DimXpertDatum annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum letter
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Datum Letter: " + annotation.Identifier);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void PositionData(DimXpertPositionTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool enabled = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double value = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Zone Type: " + PositionZoneType((long)annotation.ZoneType));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the zone vector if the tolerance zone is planar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (annotation.ZoneType == swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Direction: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Max Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the material condition modifer applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FormatProjectedZone(enabled, value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompositePositionData(DimXpertCompositePositionTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool enabled = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double value = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Zone Type: " + PositionZoneType((long)annotation.ZoneType));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the zone vector when the zone is planar
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (annotation.ZoneType == swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Direction: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the material condition modifer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FormatProjectedZone(enabled, value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame for the pattern location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame for the feature to feature location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite datums:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void SymmetryData(DimXpertSymmetryTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the material condition modifer applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the direction of the planar zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetZoneDirection(ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Direction: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void ConcentricityData(DimXpertConcentricityTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the material condition modifer applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void TotalRunoutData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr(annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CircularRunoutData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr(annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void LineProfileData(DimXpertLineProfileTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the vector normal to the profile zones
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompositeLineProfileData(DimXpertCompositeLineProfileTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double i = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double j = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double k = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the vector normal to the profile zones
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref i, ref j, ref k);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(i, j, k));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Datums:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void SurfaceProfileData(DimXpertSurfaceProfileTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the outer (outside material) tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Outer Tolerance: " + FormatDouble(annotation.OuterToleranceValue));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompositeSurfaceProfileData(DimXpertCompositeSurfaceProfileTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance Upper Tier: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the outer tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Outer Tolerance Upper Tier: " + FormatDouble(annotation.OuterToleranceValue));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame for the location
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame for the orientation and form
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Composite Datums:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Primary: " + (annotation.PrimaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Secondary: " + (annotation.SecondaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Repeat Tertiary: " + (annotation.TertiaryInLowerTier ? "True" : "False"));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void OrientationData(DimXpertOrientationTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool enabled = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double value = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e annoType = default(SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertAnnotation anno;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}anno = (DimXpertAnnotation)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = (SolidWorks.Interop.swdimxpert.swDimXpertAnnotationType_e)anno.Type;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the type or orientation tolerance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: Perpendicularity");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: Parallelism");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Orientation Type: Angularity");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (annotation.ZoneType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Cylindrical:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Type: Cylindrical");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertOrientationZoneType_e.swDimXpertOrientationZoneType_Planar:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Type: Planar");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Planar Zone Vector: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//material condition modifer applied to feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the projected tolerance zone when specified
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetProjectedZone(ref enabled, ref value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FormatProjectedZone(enabled, value);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// is tangent plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" IsTangentPlane: " + (annotation.IsTangentPlane() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr((DimXpertTolerance)annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void FlatnessData(DimXpertFlatnessTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool enabled = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double length = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double width = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the per unit area data
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitArea(ref enabled, ref length, ref width, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Per Unit Area: " + (enabled ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (enabled)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Per Unit Length: " + FormatDouble(length));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Per Unit Width: " + FormatDouble(width));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Per Unit Direction: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CircularityData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CylindricityData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void StraightnessData(DimXpertStraightnessTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool enabled = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double dist = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//tolerance compartment info
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//type or shape of the tolerance zone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (annotation.ZoneType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Cylindrical:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Type: Cylindrical");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_PlanarMedian:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Type: Planar Median");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertStraightnessZoneType_e.swDimXpertStraightnessZoneType_Surface:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Type: Surface Straightness");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlanarZoneVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Zone Vector: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//per unit length
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetPerUnitLength(ref enabled, ref dist);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Per Unit Length: " + (enabled ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (enabled)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Per Unit Length Distance: " + FormatDouble(dist));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the material condition modifer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Modifier: " + mcmStr((long)annotation.Modifier));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void ProfileData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the datum reference frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DatumsStr(annotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void SurfaceFinishData(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void TangencyData(DimXpertTangencyTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + annotation.OriginFeature.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Compartment");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the tolerance value
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertTolerance tol;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tol = (DimXpertTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Tolerance: " + FormatDouble(tol.Tolerance));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void DimensionToleranceData(DimXpertDimensionTolerance annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool isAngleType = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDimXpertAnnotationType_e annoType = default(swDimXpertAnnotationType_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDimXpertPatternTreatmentType_e patternTreatment = default(swDimXpertPatternTreatmentType_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double upper = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double lower = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double plus = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double minus = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertAnnotation anno;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}anno = (DimXpertAnnotation)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}annoType = anno.Type;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DistanceBetweenData((DimXpertDistanceBetweenDimTol)annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompositeDistanceBetweenData((DimXpertCompositeDistanceBetweenDimTol)annotation, (DimXpertPart) dimXpertPart);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertCounterBoreDimTol dimtol;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimtol = (DimXpertCounterBoreDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (dimtol.ReferenceFeature == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Depth)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertDepthDimTol dimtol;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimtol = (DimXpertDepthDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (dimtol.ReferenceFeature == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertCounterSinkDiameterDimTol dimtol;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimtol = (DimXpertCounterSinkDiameterDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (dimtol.ReferenceFeature == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertChamferDimTol chamferDimTol = default(DimXpertChamferDimTol);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}chamferDimTol = (DimXpertChamferDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (chamferDimTol.ChamferType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_Angle:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Angle");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}isAngleType = true;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Distance 1");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case swDimXpertChamferDimensionType_e.swDimXpertChamferDimensionType_LinearDistance2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension Type: Distance 2");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertAngleBetweenDimTol dimtol;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimtol = (DimXpertAngleBetweenDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// the origin and tolerance feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + dimtol.OriginFeature.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// is supplement angle
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Supplement Angle: " + (dimtol.Supplement ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertCounterSinkAngleDimTol dimtol;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimtol = (DimXpertCounterSinkAngleDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (dimtol.ReferenceFeature == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: NULL");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + dimtol.ReferenceFeature.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isAngleType = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Radius)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}IDimXpertRadiusDimTol radiusDim;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}radiusDim = (IDimXpertRadiusDimTol)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}patternTreatment = radiusDim.PatternTreatment;
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}//If radiusDim.patternTreatment Is Nothing Then
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}//strs.Add ("Pattern Treatment: NULL")
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_unknown)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{strs.Add ("Pattern Treatment: unknown");}
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_CircularPattern)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{strs.Add ("Pattern Treatment: Circular pattern");}
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_IndividualFeatures)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{strs.Add ("Pattern Treatment: Individual features");}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (annoType == swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IDimXpertDiameterDimTol diaDim;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}diaDim = (IDimXpertDiameterDimTol)annotation;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}patternTreatment = diaDim.PatternTreatment;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//If radiusDim.patternTreatment Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//strs.Add ("Pattern Treatment: NULL")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_unknown)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{ strs.Add("Pattern Treatment: unknown"); }
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_CircularPattern)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{ strs.Add("Pattern Treatment: Circular pattern"); }
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (patternTreatment == swDimXpertPatternTreatmentType_e.swDimXpertPatternTreatmentType_IndividualFeatures)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{ strs.Add("Pattern Treatment: Individual features"); }
```

```vb
Boolean indReq;
 Boolean envReq;
 indReq = diaDim.IndependencyRequirement;
 envReq = diaDim.EnvelopeRequirement;
 strs.Add("Independency is required: " + indReq.ToString());
 strs.Add("Envelope is required: " + envReq.ToString());
```

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// conversion for radians to degrees when dimension type is angle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double dbl = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (isAngleType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 57.2957795130823;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 1.0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal, and upper and lower limits of size of the dimension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Compute Nominal Dimension: " + FormatDouble(annotation.GetNominalValue() * dbl));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the upper and lower tolerance value by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (annotation.DimensionType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockTolerance:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Block Tolerance");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}DimXpertBlockTolerances blockTols = default(DimXpertBlockTolerances);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (blockTols.Type)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Dimension Type: Block Tolerance No Nominal");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}if (isAngleType)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}strs.Add("Angular Block Tolerance");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}strs.Add("Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", annotation.BlockToleranceDecimalPlaces.ToString()));
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Dimension Type: General Tolerance");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFits:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limits and Fits");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// limits and fits tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_ISOLimitsAndFitsNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limits and Fits No Nominal");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Limits and Fits: " + annotation.LimitsAndFitsCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// limit dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_LimitDimension:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Limit Dimension");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetUpperAndLowerLimit(ref upper, ref lower);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Get Upper Limit: " + FormatDouble(upper * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Get Lower Limit: " + FormatDouble(lower * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MAXTolerance:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: MAXTolerance");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_MINTolerance:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: MINTolerance");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_NoTolerance:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: NoTolerance");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusDimension:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Plus Minus Dimension");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Dimension Type: Plus Minus No Nominal");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusTolerance(ref plus, ref minus);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Plus Tolerance: " + FormatDouble(plus * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Minus Tolerance: " + FormatDouble(minus * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void DistanceBetweenData(DimXpertDistanceBetweenDimTol annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDimXpertDistanceFosUsage_e featureFosUsage = default(swDimXpertDistanceFosUsage_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(ref feature, ref featureFosUsage);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(ref feature, ref featureFosUsage);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// The direction vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Direction Vector: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompositeDistanceBetweenData(DimXpertCompositeDistanceBetweenDimTol annotation, SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDimXpertDistanceFosUsage_e featureFosUsage = default(swDimXpertDistanceFosUsage_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double plus = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double minus = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool isAngleType = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertBlockTolerances blockTols = default(DimXpertBlockTolerances);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}isAngleType = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// conversion for radians to degrees when dimension type is angle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double dbl = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (isAngleType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 57.2957795130823;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dbl = 1.0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the origin and tolerance feature along with their feature of size usage (min, max, center)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetOriginFeature(ref feature, ref featureFosUsage);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Origin Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetFeature(ref feature, ref featureFosUsage);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Tolerance Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the pattern locating feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetIntraFeature(ref feature, ref featureFosUsage);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Feature: " + feature.Name + " @ " + FosUsage(featureFosUsage));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// The direction vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = annotation.GetDirectionVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Direction Vector: " + FormatVector(I, J, K));
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the upper and lower tolerance value for the pattern location by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertDimensionTolerance dimTol = default(DimXpertDimensionTolerance);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimTol = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dimTol = (DimXpertDimensionTolerance)annotation;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (dimTol.DimensionType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: Plus Minus No Nominal");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = dimTol.GetPlusAndMinusTolerance(ref plus, ref minus);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Plus Tolerance: " + FormatDouble(plus));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Minus Tolerance: " + FormatDouble(minus));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (blockTols.Type)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: Block Tolerance No Nominal");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add(" Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", dimTol.BlockToleranceDecimalPlaces.ToString()));
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Pattern Locating Dimension Type: General Tolerance");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the upper and lower tolerance value for the feature to feature location by type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (annotation.DimensionTypeIntraFeature)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// plus and minus dimension
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_PlusMinusNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Feature Locating Dimension Type: Plus Minus No Nominal");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = annotation.GetPlusAndMinusToleranceIntraFeature(ref plus, ref minus);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Plus Tolerance: " + FormatDouble(plus * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Minus Tolerance: " + FormatDouble(minus * dbl));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// block tolerance
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDimensionToleranceType_e.swDimXpertDimTolType_BlockToleranceNoNominal:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (blockTols.Type)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Feature locating Dimension Type: Block Tolerance No Nominal");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add(" Block Tolerance Decimal Places: " +
System.String.Format("{0:N}", annotation.BlockToleranceDecimalPlacesIntraFeature.ToString()));
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}strs.Add("Feature locating Dimension Type: General Tolerance");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void DatumsStr(DimXpertTolerance annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Datums:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}datumStr((object[])annotation.GetPrimaryDatums(), (int[])annotation.GetPrimaryDatumModifiers(), " Primary:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}datumStr((object[])annotation.GetSecondaryDatums(), (int[])annotation.GetSecondaryDatumModifiers(), " Secondary:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}datumStr((object[])annotation.GetTertiaryDatums(), (int[])annotation.GetTertiaryDatumModifiers(), " Tertiary:");
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void datumStr(object[] dats, int[] mods, string datumOrder)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long mcm = 0;
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((dats == null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}for (I = dats.GetLowerBound(0); I <= dats.GetUpperBound(0); I++)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}mcm = (long)mods[I];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertDatum datum;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}datum = (DimXpertDatum)dats[I];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str = str + " " + datum.Identifier + " @ " + mcmStr(mcm);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (System.String.Compare(str, "") > 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(datumOrder + str);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(datumOrder + " <none>");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// returns a string containing the height of the projected tolerance zone
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void FormatProjectedZone(bool enabled, double height)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (enabled == true)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Projected Zone: True");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Zone Height: " + FormatDouble(height));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Projected Zone: False");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string mcmStr(long mcm)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch ((swDimXpertMaterialConditionModifier_e)mcm)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_LMC:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "LMC";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_MMC:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "MMC";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_NoMCM:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "NoMCM";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertMaterialConditionModifier_e.swDimXpertMCM_RFS:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RFS";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// returns a string containing the type of position tolerance zone used
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string PositionZoneType(long typ)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch ((swDimXpertPositionZoneType_e)typ)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_CylindricalPosition:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Cylindrical";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_PlanarPosition:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Planar";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_SphericalPosition:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Spherical";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_Boundary:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Boundary";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionArc:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RadialPositionArc";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertPositionZoneType_e.swDimXpertPositionZoneType_RadialPositionPlanar:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "RadialPositionPlanar";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "N/A";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// returns a string containing the names of the SW display entities
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string DisplayEntity(DimXpertAnnotation annotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object dispEnt = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Annotation swAnnot = default(Annotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dispEnt = annotation.GetDisplayEntity();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((dispEnt != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (dispEnt is Annotation)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAnnot = (Annotation)dispEnt;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = (String)swAnnot.GetName();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// returns a string containing the feature of size usage (min, max, center)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string FosUsage(swDimXpertDistanceFosUsage_e value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_Center:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Center";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MaximumSide:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Max";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertDistanceFosUsage_e.swDimXpertDistanceFosUsage_MinimumSide:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "Min";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = "N/A";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string FormatVector(double I, double J, double K)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = FormatDouble(I) + ", " + FormatDouble(J) + ", " + FormatDouble(K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string FormatDouble(double value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = System.String.Format("{0:D}", value.ToString());
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string RadiansToDegrees(double value)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = System.String.Format("{0:D}", (value * 57.2957795130823).ToString());
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string annotationTypeNameFromObject(DimXpertAnnotation anno)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return annotationTypeNameFromTypeNumber(anno.Type);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string annotationTypeNameFromTypeNumber(swDimXpertAnnotationType_e annoTypeIndex)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string functionReturnValue = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (annoTypeIndex)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_DistanceBetween:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "DistanceBetween Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterBore:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CounterBore Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_Depth:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Depth Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkDiameter:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CounterSinkDiameter Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_ChamferDimension:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "ChamferDimension Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_AngleBetween:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "AngleBetween Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_CounterSinkAngle:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CounterSinkAngle Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_ConeAngle:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "ConeAngle Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_Diameter:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Diameter Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_Length:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Length Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_Radius:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Radius Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_Width:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Width Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDimTol_CompositeDistanceBetween:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CompositeDistanceBetween Dim";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertDatum:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Datum";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Position:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Position Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositePosition:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CompositePosition Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Symmetry:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Symmetry Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Concentricity:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Concentricity Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_LineProfile:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "LineProfile Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeLineProfile:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CompositeLineProfile Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_SurfaceProfile:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "SurfaceProfile Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_CompositeSurfaceProfile:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CompositeSurfaceProfile Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Angularity:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Angularity Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Parallelism:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Parallelism Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Perpendicularity:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Perpendicularity Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_TotalRunout:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "TotalRunout Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_CircularRunout:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "CircularRunout Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Flatness:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Flatness Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Circularity:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Circularity Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Cylindricity:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Cylindricity Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Straightness:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Straightness Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case swDimXpertAnnotationType_e.swDimXpertGeoTol_Tangency:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Tangency Tol";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "<unknown> " + annoTypeIndex;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return functionReturnValue;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
