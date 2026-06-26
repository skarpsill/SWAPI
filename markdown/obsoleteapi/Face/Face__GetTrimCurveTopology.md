---
title: "Face::GetTrimCurveTopology"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTrimCurveTopology.htm"
---

# Face::GetTrimCurveTopology

This
method is obsolete and has been superseded by[Face2::GetTrimCurveTopology](sldworksAPI.chm::/Face2/Face2__GetTrimCurveTopology.htm).

Description

This method gets the trim curve topology for this face.

Syntax (OLE Automation)

retval
= Face.GetTrimCurveTopology ()

(Table)=========================================================

| Return: | (VARIANT)
retval | Trim
curve topology for this face |
| --- | --- | --- |

Syntax (COM)

status
= Face->IGetTrimCurveTopology ( &topolList )

(Table)=========================================================

| Output: | (LPDISPATCH*)
topolList | Trim
curve topology for this face |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method returns a list of CoEdges,
Vertex's and NULLs.

You must successfully call[GetTrimCurves2](Face__GetTrimCurves2.htm)before calling this method. If you successfully call GetTrimCurves2 prior
to this call, this method returns a list of proper edges corresponding
to the list of SP curves that GetTrimCurves2 passed back. Otherwise, this
method asks the modeler for the list of edges that it thinks are on the
face. These two lists differ in order and content.

Use[GetTrimCurveTopologyTypes](Face__GetTrimCurveTopologyTypes.htm)to get an array of types corresponding to the returned objects in topolList.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetTrimCurveTopology.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
