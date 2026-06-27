---
title: "FeatureManager::InsertFillSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertFillSurface.htm"
---

# FeatureManager::InsertFillSurface

This method is obsolete and has been superseded
by[FeatureManager::InsertFillSurface2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertFillSurface2.htm).

Description

This method inserts a fill-surface
feature in the model.

Syntax (OLE Automation)

bRet = FeatureManager.InsertFillSurface ( resolution
)

(Table)=========================================================

| Input: | (long) resolution | Controls the resolution or quality of the surface (see Remarks ) |
| --- | --- | --- |
| Output: | (LPFEATURE) bRet | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertFillSurface ( resolution,
&bRet )

Parameters Table Start

(Table)=========================================================

| Input: | (long) resolution | Controls the resolution or quality of the surface (see Remarks ) |
| --- | --- | --- |
| Output: | (LPFEATURE) bRet | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You must use ModelDocExtension::SelectByID2
and the following Mark values to select edges that bound the surface to
be filled:

- Boundary
  curves = 1
- Boundary
  with contact curvature control = 257
- Boundary
  with tangent curvature control = 513
- Constraint
  curves or internal curves = 4

The resolution argument can
be set to 1, 2, or 3. The higher the value, the better the resolution.

Use the Body2::Diagnose and
the DiagnoseResult APIs to get the gaps to fill.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertFillSurface.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$Feature_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertFillSurface.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXGetFillGaps$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertFillSurface.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
