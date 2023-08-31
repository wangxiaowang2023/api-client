# CosmosTxV1beta1BroadcastTxRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_bytes** | **str** | tx_bytes is the raw transaction. | [optional] 
**mode** | **str** | BroadcastMode specifies the broadcast mode for the TxService.Broadcast RPC method.   - BROADCAST_MODE_UNSPECIFIED: zero-value for mode ordering  - BROADCAST_MODE_BLOCK: DEPRECATED: use BROADCAST_MODE_SYNC instead, BROADCAST_MODE_BLOCK is not supported by the SDK from v0.47.x onwards.  - BROADCAST_MODE_SYNC: BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits for a CheckTx execution response only.  - BROADCAST_MODE_ASYNC: BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client returns immediately. | [optional] [default to 'BROADCAST_MODE_UNSPECIFIED']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

