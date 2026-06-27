---
title: "ModelDoc::SetLightSourceName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetLightSourceName.htm"
---

# ModelDoc::SetLightSourceName

This method is obsolete
and has been superseded by[ModelDoc2::SetLightSourceName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetLightSourceName.htm).

Description

This method sets the light source name, as used internally by SolidWorks.

Syntax (OLE Automation)

retval = ModelDoc.SetLightSourceName
( id, newName)

(Table)=========================================================

| Input: | (long) id | ID of the light source whose name you want to set |
| --- | --- | --- |
| Input: | (BSTR) newName | Name to be given to the specified light source |
| Return: | (BOOL) retval | TRUE if the name was set successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetLightSourceName
( id, newName, &retval )

(Table)=========================================================

| Input: | (long) id | ID of the light source whose name you want to set |
| --- | --- | --- |
| Input: | (BSTR) newName | Name to be given to the specified light source |
| Output: | (VARIANT_BOOL) retval | TRUE if the name was set successfully, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The light source ID ranges from 0 ton,
wheren= (the total number of
light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZLighting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetLightSourceName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
