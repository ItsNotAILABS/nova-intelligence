import Time "mo:base/Time";
actor NovaAgentsBackend {
  stable var lastReceipt : Text = "initialized";
  public query func status() : async Text { "NOVA Agent Council ICP lane alive: " # lastReceipt };
  public func stageReceipt(receipt : Text) : async Text { lastReceipt := receipt # " @ " # debug_show(Time.now()); lastReceipt };
}
