---
title: "Set Tolerances and Compare Geometry Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Set_Tolerances_and_Compare_Geometry_CSharp.htm"
---

# Set Tolerances and Compare Geometry Example (C#)

his example shows how to set the
tolerances and then compare the volume and geometry of two versions of the same
part using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference >
'    browse to install_dir\api\redist > SolidWorks.Interop.gtswutilities.dll).
' 3. Verify that the specified files exist.
' 4. Verify that C:\test\ exists.
'
' Postconditions:
' 1. Creates a geometry comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets position and angular tolerance statuses.
' 3. Gets face and volume comparison statuses.
' 4. Examine the Immediate window, graphics area, and C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'-------------------------------------------------------------------------
```

using SOLIDWORKS.Interop.sldworks;

using SOLIDWORKS.Interop.swconst;

using SOLIDWORKS.Interop.gtswutilities;

using System;

using System.Diagnostics;

namespace SetTolerancesAndCompareGeometry_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SOLIDWORKSMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PartDoc
Part;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= (PartDoc)swApp.**ActiveDoc**;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtcocswUtilities
swUtil = default(gtcocswUtilities);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtcocswCompareGeometry
swUtilCompGeom = default(gtcocswCompareGeometry);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtcocswUtilOptions
OUtils = default(gtcocswUtilOptions);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
file1 = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
file2 = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
reportname = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
errorcode = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
posTol = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
angTol = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
AddToDesignBinder = false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
OverwriteReport = false;

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}reportname
= "C:\\test\\Report";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddToDesignBinder
= false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OverwriteReport
= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get pointer to SOLIDWORKS Utilities interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtil
= (gtcocswUtilities)swApp.**GetAddInObject**("Utilities.UtilitiesApp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get pointer to SOLIDWORKS Compare Geometry tool

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtilCompGeom
= (gtcocswCompareGeometry)swUtil.GetToolInterface((int)gtSwTools_e.gtSwToolGeomDiff,
out errorcode);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get SOLIDWORKS Utilities options

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OUtils
= swUtil.options;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}posTol
= 0.0001;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Meters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}angTol
= 1E-06;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Radians

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Set position tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= OUtils.SetPositionTolerance(posTol);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Position
tolerance is set." + " gtError_e: " + errorcode);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Set angular tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= OUtils.SetAngularTolerance(angTol);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Angular
tolerance is set." + " gtError_e: " + errorcode);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
volDiffStatus = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
faceDiffStatus = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file1
= "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_a.sldprt";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file2
= "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_b.sldprt";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Compare the geometry of the faces and volumes and save results to a report

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= swUtilCompGeom.CompareGeometry3(file1,
"", file2, "", (int)gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare,
(int)gtResultOptions_e.gtResultSaveReport, reportname, AddToDesignBinder,
OverwriteReport, ref volDiffStatus,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ref
faceDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(errorcode == (int)gtError_e.gtNOErr))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
comparing geometries. Inspect gtError_e = " + errorcode + "
in the API help.");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}diffStatus("Volume
comparison", volDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}diffStatus("Face
comparison", faceDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Perform any necessary cleanup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= swUtilCompGeom.Close();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void diffStatus(string name, int diffCode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}switch
(diffCode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtSuccess:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Succeeded");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtNotPerformed:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Not
performed");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtCanceled:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Canceled");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtFailed:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Failed");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtIdenticalParts:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Identical
parts");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtDifferentParts:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Different
parts");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtNoSolidBody:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("No
solid body found");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtAlreadySaved:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Already
saved");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
