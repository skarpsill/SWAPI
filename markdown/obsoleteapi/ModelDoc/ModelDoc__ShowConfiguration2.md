---
title: "ModelDoc::ShowConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowConfiguration2.htm"
---

# ModelDoc::ShowConfiguration2

This method is obsolete
and has been superseded by[ModelDoc2::ShowConfiguration2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowConfiguration2.htm).

Description

This method displays the named configuration. Configurations allow you
to save certain display characteristics with each of the assembly components
and then retrieve that configuration at some point in the future. This
method allows you to retrieve a previously saved configuration.

Syntax (OLE Automation)

retval = ModelDoc.ShowConfiguration2
( configurationName)

(Table)=========================================================

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ShowConfiguration2
( configurationName, &retval )

(Table)=========================================================

| Input: | (BSTR) configurationName | Name of the configuration to display |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration was activated successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyObjectDisplay$$**$$ZModifyConfiguration$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__ShowConfiguration2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
