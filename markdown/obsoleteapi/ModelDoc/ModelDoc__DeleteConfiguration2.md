---
title: "ModelDoc::DeleteConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteConfiguration2.htm"
---

# ModelDoc::DeleteConfiguration2

This
method is obsolete and has been superseded by[ModelDoc2::DeleteConfiguration2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteConfiguration2.htm).

Description

This method deletes a configuration. The configuration you delete cannot
be the active configuration.

Syntax (OLE Automation)

retval = ModelDoc.DeleteConfiguration2
( configurationName)

(Table)=========================================================

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |
| Return: | VARIANT_BOOL retval | TRUE if successfully deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteConfiguration2
( configurationName, &retval )

(Table)=========================================================

| Input: | (BSTR) configurationName | Name of the configuration to delete |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully deleted, FALSE if not |
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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyConfiguration$$**$$ZDeleting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__DeleteConfiguration2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
