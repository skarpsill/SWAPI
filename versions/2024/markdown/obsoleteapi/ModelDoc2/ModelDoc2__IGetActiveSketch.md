---
title: "ModelDoc2::GetActiveSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__IGetActiveSketch.htm"
---

# ModelDoc2::GetActiveSketch

This
method is obsolete and has been superseded by ModelDoc2::GetActiveSketch2.

Description

This method returns the active sketch in document. If a sketch is not
currently active, or if the active sketch is a 3D sketch, then NULL is
returned.

Syntax (OLE Automation)

retval = ModelDoc2.GetActiveSketch
()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a sketch |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->IGetActiveSketch
( &retval )

(Table)=========================================================

| Output: | (LPSKETCH) retval | Pointer to the active Sketch object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before you can use this method, you must select
and activate a sketch. You can use ModelDoc2::SelectByID to select a sketch
and ModelDoc2::InsertSketch2 to make the sketch active.

To avoid regressions in existing applications,
this method returns NULL if the active sketch is a 3D sketch. To access
the active 2D or 3D sketch, use ModelDoc2::GetActiveSketch2. To determine
if a Sketch object is 2D or 3D, use Sketch::Is3D.

For an example of getting a sketch through Feature
traversal, see Get Sketches Example.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__IGetActiveSketch.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__IGetActiveSketch.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
