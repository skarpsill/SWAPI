---
title: "ModelDoc::DeleteCustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteCustomInfo2.htm"
---

# ModelDoc::DeleteCustomInfo2

This
method is obsolete and has been superseded by[ModelDoc2::DeleteCustomInfo2](../ModelDoc2/ModelDoc2__DeleteCustomInfo2.htm).

Description

This method deletes a custom property field that has been defined for
the document or the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc.DeleteCustomInfo2(
configuration, FieldName )

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom property |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteCustomInfo2(
configuration, FieldName, &retval)

(Table)=========================================================

| Input: | (BSTR)configuration | Name of the configuration |
| --- | --- | --- |
| Input: | (BSTR)FieldName | Name of custom property |
| Output: | (VARIANT_BOOL)retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The configuration name should be the name of one
configuration in the document. If the custom property is found on the
given configuration, then this method deletes that custom property. If
this name is an empty string, then this method attempts to delete the
custom property from the document.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__DeleteCustomInfo2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
