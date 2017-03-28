BEGIN
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'BDDSEcnReIssueBy' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'BDDSEcnReIssueDate' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'FDDSEcnReIssueBy' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'FDDSEcnReIssueDate' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'PDDSEcnReIssueBy' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'PDDSEcnReIssueDate' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'WDDSEcnReIssueBy' AND ContextName = 'A400M_ECN_Reissue_Manager';
	INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) SELECT ATTRIBUTE_id, CONTEXT_id, 1, 1 FROM T_EDIP_ATTRIBUTE, T_EDIP_CONTEXT WHERE AttributeName = 'WDDSEcnReIssueDate' AND ContextName = 'A400M_ECN_Reissue_Manager';
END