---
title: "ModelDoc::Rebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Rebuild.htm"
---

# ModelDoc::Rebuild

This
method is obsolete and has been superseded by[ModelDoc2::Rebuild](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Rebuild.htm).

Description

This method rebuilds the model.

Syntax (OLE Automation)

void ModelDoc.Rebuild ( Options )

(Table)=========================================================

| Input: | (long) Options | Type of rebuild as defined in swRebuildOptions_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Syntax (COM)

status = ModelDoc->Rebuild ( Options
)

(Table)=========================================================

| Input: | (long)O ptions | Type of rebuild as defined in swRebuildOptions_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Certain options are only valid for particular document types; use ModelDoc::GetType
to check the type of document.

Option Document Types Description

swRebuildAll All Rebuilds
geometry that has not been regenerated.

swForceRebuildAll All Forces
a rebuild of all geometry.

swUpdateMates AssemblyDoc Only
rebuilds mates, which is much faster than rebuilding the geometry. Especially
for use with Component::SetXform.

swCurrentSheetDisp DrawingDoc Only
rebuilds the display of the views on the current drawing sheet.

swUpdateDirtyOnly DrawingDoc Only
rebuilds drawing views which are dirty when "OR'd" with swCurrentSheetDisp
option.

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
<param name="Items" value="PartDoc_Object$$**$$ZEditRebuild$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__Rebuild.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
