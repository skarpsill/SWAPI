---
title: "DimXpert Feature Data Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_FeatureData_Module_CSharp.htm"
---

# DimXpert Feature Data Module Example (C#)

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
public class DimXpertFeatureData
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// Returns a collection of Strings containing the features data
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private Collection<string> strs = new Collection<string>();
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Clear(Collection<string> strs)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Remove(strs[strs.Count]);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (!(strs.Count == 0))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Clear(strs);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public Collection<string> FeatureData(DimXpertFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e featureType = default(SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((!(strs.Count == 0)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Clear(strs);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// General info, including the feature name, face id, and suppressed status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}FeatInfo(feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featureType = feature.Type;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Plane)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PlaneData((DimXpertPlaneFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert cylinder or boss. Also used for the sub-feature of a
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// compound hole (simple hole, counterbore, countersink...)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CylinderData((DimXpertCylinderFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert cone
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cone)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ConeData((DimXpertConeFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert pocket or extrude
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Extrude)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ExtrudeData((DimXpertExtrudeFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert fillet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Fillet)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FilletData((DimXpertFilletFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert chamfer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Chamfer)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ChamferData((DimXpertChamferFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert hole type (Simple, counterbore, countersink...)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompoundHoleData((DimXpertCompoundHoleFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert width
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompoundWidthData((DimXpertCompoundWidthFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert notch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompoundNotchData((DimXpertCompoundNotchFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert slot
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompoundSlot3dData((DimXpertCompoundClosedSlot3DFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert intersect point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IntersectPointData((DimXpertIntersectPointFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert intersect line
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IntersectLineData((DimXpertIntersectLineFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert intersect circle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IntersectCircleData((DimXpertIntersectCircleFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert intersect plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IntersectPlaneData((DimXpertIntersectPlaneFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert pattern (hole, slot, notch...)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Pattern)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PatternData((DimXpertPatternFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert sphere
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Sphere)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SphereData((DimXpertSphereFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert best fit plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BestfitPlaneData((DimXpertBestfitPlaneFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DimXpert surface
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else if (featureType == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Surface)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SurfaceData((DimXpertFeature)feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return strs;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void FeatInfo(DimXpertFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string featureType = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Feature modelObj = default(Feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Name: " + feature.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featureType = featureTypeNameFromObject(feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Type: " + featureType);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(GetFaceId(feature));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsSuppressed: " + (feature.IsSuppressed() ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelObj = (Feature)feature.GetModelFeature();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((modelObj != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("ModelFeature: " + modelObj.Name + " (" + modelObj.GetTypeName2() + ")");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void PlaneData(DimXpertPlaneFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// list the plane's nominal point and vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CylinderData(DimXpertCylinderFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool isThreaded = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string threadDesignation = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double threadDepth = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double R = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isInner status, is the feature a hole or boss?
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}threadDesignation = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isThreaded status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetThread(ref isThreaded, ref threadDesignation, ref threadDepth);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsThreaded: " + (isThreaded ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// thread designation and depth
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (isThreaded)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Thread Designation: " + threadDesignation);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Thread Depth: " + FormatDouble(threadDepth));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the cylinder's diameter, axis point, and vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Cylinder:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalCylinder(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Diameter: " + FormatDouble(R * 2));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal top plane of the cylinder, which is the highest point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// of the cylinder's boundary projected onto its axis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Top Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal bottom plane of the cylinder, which is the lowest point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// of the cylinder's boundary projected onto its axis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Bottom Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void ConeData(DimXpertConeFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Angle = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//the nominal cone's angle, axis point, and vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Cone:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalCone(ref Angle, ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Cone Angle: " + RadiansToDegrees(Angle));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal top plane of the cone, which is the highest point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// of the cone's boundary projected onto its axis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Top Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal bottom plane of the cone, which is the lowest point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// of the cone's boundary projected onto its axis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Bottom Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void FilletData(DimXpertFilletFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//the fillet radius
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Radius: " + FormatDouble(feature.Radius));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void ChamferData(DimXpertChamferFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// chamfer dimension scheme, which can be a distance and an angle, or 2 distances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (feature.ChamferType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_DistanceAngle:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension: Distance and Angle");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Distance: " + FormatDouble(feature.Distance1));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Angle: " + RadiansToDegrees(feature.Angle));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_DistanceDistance:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Chamfer Dimension: 2 Distances");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Distance1: " + FormatDouble(feature.Distance1));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" Distance2: " + FormatDouble(feature.Distance2));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertChamferType_e.swDimXpertChamferType_Vertex:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add("Chamfer Type: Vertex");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompoundHoleData(DimXpertCompoundHoleFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double R = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long index = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature featObj = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the type of compound hole
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string typ = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}typ = "";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (feature.CompoundHoleType)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Counterbore:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}typ = "Counterbore";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Countersink:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}typ = "Countersink";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Compound:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}typ = "Compound";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Simple:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}typ = "Simple";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Hole Type: " + typ);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// is blind status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// reference plane, which is the basis for all depth tolerances
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetReferenceFeature() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + feature.GetReferenceFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Reference Feature: isNothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// bottom feature, used for the depth of blind holes
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetBottomFeature() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Feature: isNothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//get the collection of sub-features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] subFeats = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}subFeats = (object[])feature.GetSubFeatures();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the collection of sub-features that make up the hole
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("" + "Sub-Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (!((subFeats == null)))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = subFeats.GetLowerBound(0); index <= subFeats.GetUpperBound(0); index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featObj = (DimXpertFeature)subFeats[index];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" " + featObj.Name + "");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// the location of the hole based on the first cylinder in the list of sub-feaures
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = subFeats.GetLowerBound(0); index <= subFeats.GetUpperBound(0); index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featObj = (DimXpertFeature)subFeats[index];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (featObj.Type == SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}DimXpertCylinderFeature cylFeat = default(DimXpertCylinderFeature);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cylFeat = (DimXpertCylinderFeature)featObj;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}boolstatus = cylFeat.GetNominalCylinder(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// the diameter of the hole for type simple
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}switch (feature.CompoundHoleType)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertCompoundHoleType_e.swDimXpertCompoundHoleType_Simple:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}strs.Add("Diameter: " + FormatDouble(R * 2));
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add("Nominal Axis:");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}index = subFeats.GetUpperBound(0);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompoundWidthData(DimXpertCompoundWidthFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double width = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two side features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((plane1 != null) & (plane2 != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature feat1 = (DimXpertFeature)plane1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature feat2 = (DimXpertFeature)plane2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Plane1: " + feat1.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Plane2: " + feat2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal width and mid-plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Width:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalCompoundWidth(ref width, ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Width: " + FormatDouble(width));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the width's longitudinal direction
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalLongitude(ref I, ref J, ref K );
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Longitudinal Direction: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompoundSlot3dData(DimXpertCompoundClosedSlot3DFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature end1 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature end2 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeI = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeJ = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeK = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double width = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double length = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//isBlind status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two side features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feat1 = (DimXpertFeature)plane1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feat2 = (DimXpertFeature)plane2;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Side1: " + feat1.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Side2: " + feat2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//the two end features, which can be cylinders or planes
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}end1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}end2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetEndFeatures(ref end1, ref end2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" End1: " + end1.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" End2: " + end2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// bottom feature, used for the depth of blind holes
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetBottomFeature() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Feature: isNothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the size and location of the nominal slot
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalClosedSlot(ref width, ref length, ref X, ref Y, ref Z, ref I, ref J, ref K, ref longitudeI, ref longitudeJ,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ref longitudeK);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Slot:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Width: " + FormatDouble(width));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Length: " + FormatDouble(length));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Axis Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Axis Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Longitudinal Vector: " + FormatABC(longitudeI, longitudeJ, longitudeK));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal top plane of the slot
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Top Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalTopPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal bottom plane of the slot
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Bottom Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void CompoundNotchData(DimXpertCompoundNotchFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeI = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeJ = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double longitudeK = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double width = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double length = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isBlind status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the reference feature or top of the notch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Top Reference Feature: " + feature.GetTopReferenceFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the open side reference feature, which bounds the notch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Open Side Reference Feature: " + feature.GetOpenSideReferenceFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two side features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Features:" + "");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feat1 = (DimXpertFeature)plane1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feat2 = (DimXpertFeature)plane2;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Side1: " + feat1.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Side2: " + feat2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the end features, which can be a cylinder or a plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetEndFeature() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" End Feature: " + feature.GetEndFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" End Feature: isNothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// bottom feature, used for the depth of blind holes
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetBottomFeature() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Bottom Feature: " + feature.GetBottomFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" Bottom Feature: isNothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal size and location of the notch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalNotch(ref width, ref length, ref X, ref Y, ref Z, ref I, ref J, ref K, ref longitudeI, ref longitudeJ,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ref longitudeK);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Notch:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Width: " + FormatDouble(width));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Length: " + FormatDouble(length));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Plane Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Longitudinal Vector: " + FormatABC(longitudeI, longitudeJ, longitudeK));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal bottom plane of the notch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Bottom Plane:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalBottomPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void ExtrudeData(DimXpertExtrudeFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long index = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] wallFeats = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature featObj = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// isBlind status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsBlind: " + (feature.Blind ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the reference feature or top plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Reference Feature: " + feature.GetReferenceFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the bottom feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Bottom Feature: " + feature.GetBottomFeature().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the top blends (fillets or chamfers)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetTopBlends() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Top Blends: " + feature.GetTopBlends().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Top Blends: Is_Nothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the bottom blends
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature.GetBottomBlends() != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Blends: " + feature.GetBottomBlends().Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Bottom Blends: Is_Nothing");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the wall features of the pocket or extrude
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Wall Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}wallFeats = (object[])feature.GetSubFeatures();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((wallFeats != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = wallFeats.GetLowerBound(0); index <= wallFeats.GetUpperBound(0); index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featObj = (DimXpertFeature)wallFeats[index];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" " + featObj.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void IntersectPointData(DimXpertIntersectPointFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature1 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature2 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two features that make up the intersect point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetFeatures(ref feature1, ref feature2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature1 != null) & (feature2 != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Sub-Features:" + "");
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feature1.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feature2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal point
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalPoint(ref X, ref Y, ref Z);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Intersect Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal vector
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalVector(ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Point Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void IntersectLineData(DimXpertIntersectLineFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane2 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two features that make up the intersect line
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetPlaneFeatures(ref plane1, ref plane2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((plane1 != null) & (plane2 != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Sub-Features:" + "");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature feat1 = (DimXpertFeature)plane1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature feat2 = (DimXpertFeature)plane2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feat1.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feat2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal line
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalLine(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Line:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void IntersectCircleData(DimXpertIntersectCircleFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertPlaneFeature plane1 = default(DimXpertPlaneFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double R = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}plane1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetPlaneFeature(ref plane1);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((plane1 != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature feat = (DimXpertFeature)plane1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Plane Feature: " + feat.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalCircle(ref R, ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Circle:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Diameter: " + FormatDouble(R * 2));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void IntersectPlaneData(DimXpertIntersectPlaneFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature1 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature feature2 = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double J = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double K = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the two features that make up the intersect plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature1 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feature2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetFeatures(ref feature1, ref feature2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((feature1 != null) & (feature2 != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add("Sub-Features:");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feature1.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strs.Add(" " + feature2.Name);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the nominal plane
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Plane");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalPlane(ref X, ref Y, ref Z, ref I, ref J, ref K);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Vector: " + FormatABC(I, J, K));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void PatternData(DimXpertPatternFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] afeats = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature featObj = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long index = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Pattern Type: " + featureTypeNameFromTypeNumber(feature.PatternType));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// list the collection of features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}afeats = (object[])feature.GetSubFeatures();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Sub-Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((afeats != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = afeats.GetLowerBound(0); index <= afeats.GetUpperBound(0); index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featObj = (DimXpertFeature)afeats[index];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" " + featObj.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void SphereData(DimXpertSphereFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double R = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double X = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Y = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}double Z = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//isInner status
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("IsInner: " + (feature.Inner ? "True" : "False"));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//the nominal sphere's radius and x, y, and z
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Nominal Sphere:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = feature.GetNominalSphere(ref R, ref X, ref Y, ref Z);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Radius: " + R);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add(" Point: " + FormatABC(X, Y, Z));
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void BestfitPlaneData(DimXpertBestfitPlaneFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] afeats = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DimXpertFeature featObj = default(DimXpertFeature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long index = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// list the collection of features
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}afeats = (object[])feature.GetSubFeatures();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Sub-Features:");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((afeats != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = afeats.GetLowerBound(0); index <= afeats.GetUpperBound(0); index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featObj = (DimXpertFeature)afeats[index];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strs.Add(" " + featObj.Name);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private void SurfaceData(DimXpertFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strs.Add("Surface Feature...");
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string FormatABC(double a, double b, double c)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = FormatDouble(a) + ", " + FormatDouble(b) + ", " + FormatDouble(c);
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
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string GetFaceId(DimXpertFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string str = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] vFaceArr = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Face2 swFace2 = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long lFeatId = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}long I = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str = "Face ID:";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vFaceArr = (Object[])feature.GetFaces();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if ((vFaceArr != null))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (I = vFaceArr.GetUpperBound(0); I <= vFaceArr.GetUpperBound(0); I++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFace2 = (Face2)vFaceArr[I];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}lFeatId = swFace2.GetFeatureId();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}str = str + " " + System.String.Format("{0:N}", lFeatId.ToString());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str = str + " <Nothing>";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return str;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string featureTypeNameFromObject(DimXpertFeature feature)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return featureTypeNameFromTypeNumber(feature.Type);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private string featureTypeNameFromTypeNumber(SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e featureTypeIndex)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string functionReturnValue = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (featureTypeIndex)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Plane:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Plane";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cylinder:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Cylinder";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Cone:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Cone";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Extrude:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Extrude";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Fillet:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Fillet";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Chamfer:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Chamfer";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Compound Hole";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Compound Width";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Compound Notch";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Compound Closed Slot";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "IntersectPoint";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "IntersectLine";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "IntersectCircle";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "IntersectPlane";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Pattern:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Pattern";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Sphere:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Sphere";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Best Fit Plane";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case SolidWorks.Interop.swdimxpert.swDimXpertFeatureType_e.swDimXpertFeature_Surface:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "Surface";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = "<unknown> " + featureTypeIndex;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return functionReturnValue;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
