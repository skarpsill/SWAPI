---
title: "ModelDoc::InsertCurveFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFile.htm"
---

# ModelDoc::InsertCurveFile

This
method is obsolete and has been superseded by[ModelDoc2::InsertCurveFile](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFile.htm).

Description

This method creates a 3D-reference curve. This reference curve goes
through the points in the specified file.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFile (
fileName)

(Table)=========================================================

| Input: | (BSTR) fileName | Filename containing the point data |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the curve is created successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertCurveFile
( fileName, &retval )

(Table)=========================================================

| Input: | (BSTR) fileName | Filename containing the point data |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the curve is created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The points in the specified input file
can have the X, Y, Z values separated by commas, spaces, or tabs, and
there should be one point per line.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateCurve$$**$$ZCreate3DCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertCurveFile.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
