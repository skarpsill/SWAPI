---
title: "ModelDoc2::SetAddToDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SetAddToDB.htm"
---

# ModelDoc2::SetAddToDB

This method is obsolete and has been superseded
by[SketchManager::AddToDB](sldworksAPI.chm::/SketchManager/SketchManager__AddToDB.htm).

Description

This method sets whether sketch entities are added directly to the SolidWorks
database.

Syntax (OLE Automation)

void ModelDoc2.SetAddToDB ( setting)

(Table)=========================================================

| Input: | (BOOL) setting | TRUE to add items directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SetAddToDB (
setting )

(Table)=========================================================

| Input: | (VARIANT_BOOL) setting | TRUE to add items directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

One of the benefits of adding sketch entities directly to the database
is that you can avoid grid and entity snapping. For example, if you create
a sketch line whose endpoint is near another entity or near a grid point,
the new line endpoint snaps to the other item or grid point. Setting ModelDoc2::SetAddToDB
to TRUE avoids this behavior during sketch entity creation.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded also increase
performance during sketch entity creation. ModelDoc2::SetDisplayWhenAdded
requires that ModelDoc2::SetAddToDB is TRUE.

If you want to constrain all the sketch entities after creation, use
Sketch::ConstrainAll.

After setting ModelDoc2::SetAddToDB to TRUE, you must set it back to
FALSE to restore SolidWorks to its normal operating mode.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetAddToDB.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$SketchDBDisplay$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetAddToDB.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXGetAssemblyBoundingBox$$**$$EXCalcClosestDistanceFaces$$**$$EXCreatePlane3Points$$**$$EXIntersectFaceEdge$$**$$EXIntersectFaces$$**$$EXClosestDistanceBetweenModelComponents$$**$$EXGetBox$$**$$EXTessellateBody$$**$$EXCreateBlockDefinitionCSharp$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetAddToDB.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
